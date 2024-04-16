import requests
import os
import random
import sys
import apiservice
from flask import Flask, url_for, render_template, redirect, session, request, jsonify
from flask_session import Session
from helpers import login_required
from datetime import datetime
from werkzeug.utils import secure_filename
from datetime import datetime
from urllib.parse import unquote


user_api = apiservice.Users()
post_api = apiservice.Posts()

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["UPLOAD_FOLDER"] = "static/uploads/user-images"
app.config["POST_IMAGE_UPLOAD_FOLDER"] = "static/uploads/post-images"
Session(app)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def path_contains(string):
    if request.referrer:
        return True if string in unquote(request.referrer) else False
    else:
        return True if string in unquote(request.path) else False

def get_post_template():
    user = user_api.findById(session["user_id"])
    post = user_api.findPostsByUserId(user["id"], order_by_date=False)[0]
    return render_template("base-post.html", post=post, user=user)

def get_posts_template(source="all"):
    user = user_api.findById(session["user_id"])
    match source:
        case "all":
            posts = post_api.findAllOrderByDateDesc()
        case "following":
            posts = user_api.getFollowingPosts(session["user_id"])
    return render_template("base-posts.html", posts=posts, user=user, path_contains=path_contains)

def get_user_profile_template(otherId):
    user = user_api.findById(session["user_id"])
    userProfile = user_api.findById(otherId)
    return render_template("base-user-profile.html", user=user, userProfile=userProfile)

@app.route("/")
@login_required
def linkup():
    return redirect(url_for("index", source="all"))

@app.route("/linkup/source=<source>", methods=["GET", "POST"])
@login_required
def index(source):
    user = user_api.findById(session["user_id"])
    posts = post_api.findAllOrderByDateDesc()
    if request.method == "GET":
        match source:
            case "all":
                posts = post_api.findAllOrderByDateDesc()
            case "following":
                posts = user_api.getFollowingPosts(session["user_id"])
            case _:
                posts = post_api.findAllOrderByDateDesc()
            
    elif request.method == "POST":
        if "searchForm" in request.form:
            option = request.form.get("flexRadioDefault")
            query = request.form.get("searchQuery")
            if query:
                match option:
                    case "users":
                        return redirect(url_for("search_users", query=query))
                    case "posts":
                        return redirect(url_for("search_posts", query=query))

    
    return render_template("layout.html", user=user, posts=posts, path_contains=path_contains)

@app.route("/create-post", methods=["POST"])
def create_post():
    title = request.form.get("title")
    body = request.form.get("body")
    imgFile = request.files.get("postImageFile")

    if imgFile:
        random.seed(datetime.now().timestamp())
        rand = random.randint(1, sys.maxsize)
        finalName = str(rand) + "." + imgFile.filename.split(".")[1]
        if allowed_file(imgFile.filename):
                    imgFile.save(os.path.join(app.config["POST_IMAGE_UPLOAD_FOLDER"], finalName))

        post_api.insert(session["user_id"], body={"title": title, "body": body, "imgUrl": finalName})
    else:
        post_api.insert(session["user_id"], body={"title": title, "body": body})

    return get_post_template()

@app.route("/delete-post/<post_id>", methods=["POST"])
def delete_post(post_id):
    if (post_api.findById(post_id)["imgUrl"]):
        os.remove(os.path.join(app.config["POST_IMAGE_UPLOAD_FOLDER"], post_api.findById(post_id)["imgUrl"]))
    post_api.delete(post_id)
    return get_posts_template()
    
@app.route("/create-comment/<post_id>/source=<source>", methods=["POST"])
def create_comment(post_id, source):
    body = request.form.get("body")
    user_api.comment(session["user_id"], post_id, body={"body": body})
    return get_posts_template(source)

@app.route("/delete-comment/<post_id>/<comment_id>/source=<source>", methods=["GET"])
def delete_comment(post_id, comment_id, source):
    user_api.deleteComment(session["user_id"], post_id, comment_id)
    return get_posts_template(source)

@app.route("/handle-like/<action>/<post_id>/source=<source>")
def handle_like(action, post_id, source):
    match action:
        case "like":
            user_api.like(session["user_id"], post_id)
        case "unlike":
            user_api.unlike(session["user_id"], post_id)
    return get_posts_template(source)

@app.route("/handle-follow/<action>/<other_id>")
@login_required
def handle_follow(action, other_id):
    match action:
        case "follow":
            user_api.follow(session["user_id"], other_id)
        case "unfollow":
            user_api.unfollow(session["user_id"], other_id)

    return get_user_profile_template(other_id)


@app.route("/edit-post/<post_id>", methods=["POST"])
def edit_post(post_id):
    title = request.form.get("title")
    body = request.form.get("body")

    if title and body:
        post_api.edit(post_id, body={"title": title, "body": body})

    return get_posts_template()

@app.route("/searchUsers?name=<query>", methods=["GET", "POST"])
@login_required
def search_users(query):
    if request.method == "GET":
        user = user_api.findById(session["user_id"])
        users = user_api.findByName(query)
        return render_template("searchUsers.html", users=users, user=user, query=query)
    elif request.method == "POST": 
        if "searchForm" in request.form:
            option = request.form.get("flexRadioDefault")
            query = request.form.get("searchQuery")
            if query:
                match option:
                    case "users":
                        return redirect(url_for("search_users", query=query))
                    case "posts":
                        return redirect(url_for("search_posts", query=query))

@app.route("/searchPosts?query=<query>", methods=["GET", "POST"])
@login_required
def search_posts(query):
    if request.method == "GET":
        user = user_api.findById(session["user_id"])
        posts = post_api.findByFullSearch(query)
        return render_template("searchPosts.html", posts=posts, user=user, query=query)
    elif request.method == "POST":
        if "searchForm" in request.form:
            option = request.form.get("flexRadioDefault")
            query = request.form.get("searchQuery")
            if query:
                match option:
                    case "users":
                        return redirect(url_for("search_users", query=query))
                    case "posts":
                        return redirect(url_for("search_posts", query=query))

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        if not request.form.get("email") or not request.form.get("password"):
            return redirect(url_for("login"))

        obj = user_api.findByEmail(request.form.get("email"))
        email = obj["email"]
        password = obj["password"]

        if email == request.form.get("email") and password == request.form.get("password"):
            session["user_id"] = obj["id"]
            return redirect(url_for("index", source="all"))
        else:
            return redirect(url_for("login"))

    else:
        return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not username or not password:
            return "Fill the username field"
        elif not password:
            "Fill the password field"

        if not requests.get("http://localhost:8080/users/" + f"search?email={email}"):
            user_api.insert(body={"name": username,
                                  "password": password,
                                  "email": email})
            obj = user_api.findByEmail(email)
            session["user_id"] = obj["id"]
            return redirect(url_for("index", source="all"))

@app.route("/edit-profile", methods=["GET", "POST"])
@login_required
def editProfile():
    if request.method == "GET":
        user = user_api.findById(session["user_id"])
        return render_template("editProfile.html", user=user)
    elif request.method == "POST":
        if "editProfile" in request.form:
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")
            imgUrl = request.files["file"].filename
            description = request.form.get("description")
            birthDate = request.form.get("birthDate")
            imgFile = request.files["file"]

            if allowed_file(imgUrl):
                filename = session["user_id"] + "." + imgFile.filename.split(".")[1]
                imgFile.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            user_api.edit(session["user_id"], body={"name": username,
                                                    "email": email,
                                                    "password": password,
                                                    "imgUrl": filename,
                                                    "description": description,
                                                    "birthDate": birthDate
                                                    })
            return redirect(url_for("index", source="all"))

        elif "searchForm" in request.form:
            option = request.form.get("flexRadioDefault")
            query = request.form.get("searchQuery")
            if query:
                match option:
                    case "users":
                        return redirect(url_for("search_users", query=query))
                    case "posts":
                        return redirect(url_for("search_posts", query=query))


@app.route("/profiles/<userId>", methods=["GET", "POST"])
def viewProfile(userId):
    user = user_api.findById(session["user_id"])
    userProfile = user_api.findById(userId)
    posts = user_api.findPostsByUserId(userId, order_by_date=True)
    if request.method == "GET":
        return render_template("profileDetails.html", userProfile=userProfile,
                               user=user, posts=posts)
    elif request.method == "POST":
        if "searchForm" in request.form:
            option = request.form.get("flexRadioDefault")
            query = request.form.get("searchQuery")
            if query:
                match option:
                    case "users":
                        return redirect(url_for("search_users", query=query))
                    case "posts":
                        return redirect(url_for("search_posts", query=query))

@app.template_filter('time_passed')
def time_passed_filter(date_string):
    date = datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")
    now = datetime.now()
    difference = now - date
    days = difference.days
    hours = difference.seconds // 3600
    minutes = (difference.seconds % 3600) // 60
    seconds = difference.seconds % 60

    if difference.total_seconds() < 60:
        return f"{seconds} second{'s' if seconds > 1 else ''} ago"
    elif difference.total_seconds() < 3600:
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    elif days > 365:
        years = days // 365
        return f"{years} year{'s' if years > 1 else ''} ago"
    elif days > 30 and days < 365:
        months = days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"
    elif days > 7 and days < 30:
        weeks = days // 7
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    elif days > 1 and days < 7:
        return f"{days} day{'s' if days > 1 else ''} and {hours} hour{'s' if hours > 1 else ''} ago"
    elif days == 1:
        return "1 day ago"
    elif hours >= 1:
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    else:
        return "less than an hour ago"

if __name__ == "__main__":
    app.run(debug=True)
