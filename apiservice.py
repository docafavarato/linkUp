import requests

class Users:
    def __init__(self):
        self.BASE_URL = "http://localhost:8080/users"

    def findAll(self) -> dict:
        return requests.get(self.BASE_URL).json()
    
    def findById(self, id: str) -> dict:
        return requests.get(self.BASE_URL + f"/{id}").json()
    
    def findPostsByUserId(self, id: str, order_by_date: bool) -> dict:
        return requests.get(self.BASE_URL + f"/{id}/posts?orderByDate={order_by_date}").json()
    
    def findCommentsByUserId(self, id: str) -> dict:
        return requests.get(self.BASE_URL + f"/{id}/comments").json()
    
    def findByName(self, name: str) -> dict:
        return requests.get(self.BASE_URL + f"/search?userName={name}").json()
    
    def findByEmail(self, email: str) -> dict:
        return requests.get(self.BASE_URL + f"/search?email={email}").json()
    
    def like(self, user_id: str, post_id: str) -> None:
        req = requests.get(self.BASE_URL + f"/{user_id}/like?postId={post_id}")

    def unlike(self, user_id: str, post_id: str) -> None:
        req = requests.get(self.BASE_URL + f"/{user_id}/unlike?postId={post_id}")

    def follow(self, user_id: str, other_id: str) -> None:
        req = requests.get(self.BASE_URL + f"/{user_id}/follow?userId={other_id}")

    def unfollow(self, user_id: str, other_id: str) -> None:
        req = requests.get(self.BASE_URL + f"/{user_id}/unfollow?userId={other_id}")

    def comment(self, user_id: str, post_id: str, body: dict) -> None:
        req = requests.post(self.BASE_URL + f"/{user_id}/comment?postId={post_id}", json=body)

    def deleteComment(self, user_id: str, post_id: str, comment_id: str) -> None:
        req = requests.delete(self.BASE_URL + f"/{user_id}/deleteComment?postId={post_id}&commentId={comment_id}")

    def getFollowingPosts(self, user_id: str) -> dict:
        return requests.get(self.BASE_URL + f"/{user_id}/followingPosts").json()
    
    def getLikedPosts(self, user_id: str) -> list:
        return requests.get(self.BASE_URL + f"/{user_id}/likedPosts").json()
    
    def getFollowers(self, user_id: str) -> list:
        return requests.get(self.BASE_URL + f"/{user_id}/followers").json()
    
    def getFollowing(self, user_id: str) -> list:
        return requests.get(self.BASE_URL + f"/{user_id}/following").json()
    
    def insert(self, body: dict) -> None:
        req = requests.post(self.BASE_URL + "/insert", json=body)

    def edit(self, user_id: str, body: dict) -> None:
        req = requests.put(self.BASE_URL + f"/{user_id}", json=body)
    
    def delete(self, user_id: str) -> None:
        req = requests.delete(self.BASE_URL + f"/{user_id}")

class Posts():
    def __init__(self):
        self.BASE_URL = "http://localhost:8080/posts"

    def findAll(self) -> dict:
        return requests.get(self.BASE_URL).json()
    
    def findById(self, id: str) -> dict:
        return requests.get(self.BASE_URL + f"/{id}").json()
    
    def findAllOrderByDateDesc(self):
        return requests.get(self.BASE_URL + "/orderByDate").json()
    
    def findByFullSearch(self, query: str) -> dict:
        return requests.get(self.BASE_URL + f"/fullSearch?text={query}").json()
    
    def findCommentsById(self, post_id: str) -> dict:
        return requests.get(self.BASE_URL + f"/{post_id}/comments").json()
    
    def findByTag(self, tag: str) -> list:
        return requests.get(self.BASE_URL + f"/searchByTag?tag={tag}").json()

    def insert(self, user_id: str, body: dict) -> None:
        req = requests.post(self.BASE_URL + f"/insert?userId={user_id}", json=body)

    def edit(self, post_id: str, body: dict) -> None:
        req = requests.put(self.BASE_URL + f"/{post_id}", json=body)

    def delete(self, post_id: str) -> None:
        req = requests.delete(self.BASE_URL + f"/{post_id}")

class Tags:
    def __init__(self):
        self.BASE_URL = "http://localhost:8080/tags"
        
    def findAll(self) -> dict:
        return requests.get(self.BASE_URL).json()
    
    def findById(self, id: str) -> dict:
        return requests.get(self.BASE_URL + f"/{id}").json()
    
    def findByName(self, name: str) -> dict:
        return requests.get(self.BASE_URL + f"/search?name={name}").json()
    
    def findTrending(self, limit: int) -> list:
        return requests.get(self.BASE_URL + f"/trending?limit={limit}").json()
    
    def insert(self, body: dict) -> None:
        requests.post(self.BASE_URL + "/insert", json=body)