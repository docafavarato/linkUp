from flask import Flask, url_for, render_template, redirect, session, request, jsonify
from flask_session import Session
from helpers import login_required
from datetime import datetime
from werkzeug.utils import secure_filename
import requests
import os

USERS_URL = "http://localhost:8080/users/"
POSTS_URL = "http://localhost:8080/posts"
COMMENTS_URL = "http://localhost:8080/comments"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["UPLOAD_FOLDER"] = "static/uploads/user-images"
app.config["POST_IMAGE_UPLOAD_FOLDER"] = "static/uploads/post-images"
Session(app)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
@login_required
def linkup():
    return redirect(url_for("index", source="all"))

@app.route("/linkup/<string:source>", methods=["GET", "POST"])
@login_required
def index(source):
    user = requests.get(USERS_URL + session["user_id"]).json()
    posts = requests.get(POSTS_URL + "/orderByDate").json()
    if request.method == "GET":
        match source:
            case "all":
                posts = requests.get(POSTS_URL + "/orderByDate").json()
            case "following":
                posts = requests.get(USERS_URL + f"{session['user_id']}/followingPosts").json()
            case _:
                posts = requests.get(POSTS_URL + "/orderByDate").json()
            
    elif request.method == "POST":
        if "commentForm" in request.form:
            postId = request.form.get("postId")
            body = request.form.get("triggerCommentBody")
            if body:
                req = requests.post(USERS_URL + f"{session['user_id']}/comment?postId={postId}", json={"body": body})
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

    
    return render_template("layout.html", user=user, posts=posts)
    

@app.route("/handle-post-image", methods=["POST"])
def handle_post_image():
    imgFile = request.files["postImageFile"]
    finalName = request.form.get("finalName")
    if allowed_file(imgFile.filename):
                imgFile.save(os.path.join(app.config["POST_IMAGE_UPLOAD_FOLDER"], finalName))
    return imgFile.filename + "saved"

@app.route("/searchUsers?name=<query>", methods=["GET", "POST"])
@login_required
def search_users(query):
    if request.method == "GET":
        user = requests.get(USERS_URL + session["user_id"]).json()
        users = requests.get(f"http://localhost:8080/users/search?userName={query}").json()
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
        user = requests.get(USERS_URL + session["user_id"]).json()
        posts = requests.get(POSTS_URL + f"/fullSearch?text={query}").json()
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

@app.route("/linkup/post/edit", methods=["POST"])
@login_required
def edit_post():
    title = request.form.get("title")
    body = request.form.get("body")

    if title and body:
        postId = request.form.get("postId")
        requests.put(POSTS_URL + f"/{postId}", json={"title": title, "body": body})

    return redirect(url_for("index", source="all"))

@app.route("/getPosts", methods=["POST"])
def get_posts():
    data = request.json
    title = data.get("title")
    body = data.get("body")
    imgUrl = data.get("imgUrl")
    req = requests.post(POSTS_URL + f"/insert?userId={session['user_id']}", json={"title": title, "body": body, "imgUrl": imgUrl})

    post = requests.get(USERS_URL + f"{session['user_id']}/posts?orderByDate=false").json()[0]
 
    return post

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        if not request.form.get("email") or not request.form.get("password"):
            return redirect(url_for("login"))

        obj = requests.get(USERS_URL + f"search?email={request.form.get('email')}").json()
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

        if not requests.get(USERS_URL + f"search?email={email}"):
            requests.post(USERS_URL + "insert", json={"name": username,
                                                      "password": password,
                                                      "email": email})
            obj = requests.get(USERS_URL + f"search?email={email}").json()
            session["user_id"] = obj["id"]
            return redirect(url_for("index", source="all"))


@app.route("/edit-profile", methods=["GET", "POST"])
@login_required
def editProfile():
    if request.method == "GET":
        obj = requests.get(USERS_URL + session["user_id"]).json()
        return render_template("editProfile.html", user=obj)
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

            requests.put(USERS_URL + session["user_id"], 
                        json={"name": username, "email": email, 
                            "password": password, "imgUrl": filename,
                            "description": description, "birthDate": birthDate})
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
    user = requests.get(USERS_URL + session["user_id"]).json()
    userProfile = requests.get(USERS_URL + userId).json()
    posts = requests.get(USERS_URL + f"{userId}/posts").json()
    if request.method == "GET":
        return render_template("profileDetails.html", userProfile=userProfile,
                               user=user, posts=posts)
    elif request.method == "POST":
        if "commentForm" in request.form:
            body = request.form.get("triggerCommentBody")
            postId = request.form.get("postId")

            if body:
                requests.post(USERS_URL + f"{session['user_id']}/comment?postId={postId}",
                              json={"body": body})

            return redirect(url_for("viewProfile", userId=userId))
        
        elif "searchForm" in request.form:
            option = request.form.get("flexRadioDefault")
            query = request.form.get("searchQuery")
            if query:
                match option:
                    case "users":
                        return redirect(url_for("search_users", query=query))
                    case "posts":
                        return redirect(url_for("search_posts", query=query))

@app.route("/delete/post/<postId>?fromPage=<fromPage>")
@login_required
def deletePost(postId, fromPage):
    req = requests.delete(POSTS_URL + f"/{postId}")
    match fromPage:
        case "index":
            return redirect(url_for("index", source="all"))
        case "profileDetails":
            return redirect(url_for("viewProfile", userId=session["user_id"]))

@app.route("/delete/comment/<commentId>/<postId>?fromPage=<fromPage>")
@login_required
def deleteComment(postId, commentId, fromPage):
    req = requests.delete(USERS_URL + f"{session['user_id']}/deleteComment?postId={postId}&commentId={commentId}")
    userProfileId = request.args.get('profileId')
    match fromPage:
        case "index":
            return redirect(url_for("index", source="all"))
        case "profileDetails":
            return redirect(url_for("viewProfile", userId=userProfileId))

@app.route("/like/post/<postId>?page=<fromPage>&otherId=<otherId>")
@login_required
def likePost(postId, fromPage, otherId):
    userId = session["user_id"]
    req = requests.get(USERS_URL + f"{userId}/like?postId={postId}")
    match fromPage:
        case "index":
            return redirect(url_for("index", source="all"))
        case "profileDetails":
            return redirect(url_for("viewProfile", userId=otherId))

@app.route("/unlike/post/<postId>?page=<fromPage>&otherId=<otherId>")
@login_required
def unlikePost(postId, fromPage, otherId):
    userId = session["user_id"]
    req = requests.get(USERS_URL + f"{userId}/unlike?postId={postId}")
    match fromPage:
        case "index":
            return redirect(url_for("index", source="all"))
        case "profileDetails":
            return redirect(url_for("viewProfile", userId=otherId))

@app.route("/<task>/<otherId>")
@login_required
def handleFollow(otherId, task):
    userId = session["user_id"]
    match task:
        case "follow":
            req = requests.get(USERS_URL + f"{userId}/follow?userId={otherId}")
        case "unfollow":
            req = requests.get(USERS_URL + f"{userId}/unfollow?userId={otherId}")

    return redirect(url_for('viewProfile', userId=otherId))


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
