import requests

post_data = []

class Post:
    def __init__(self, id, body, title, subtitle):
        self.id = id
        self.body = body
        self.title = title,
        self.subtitle = subtitle

post_url = "https://api.npoint.io/f1408ffd5819f12a34bc"


def get_posts():
    response = requests.get(post_url)
    all_posts = response.json()
    for post in all_posts:
        id = post["id"]
        body = post["body"]
        title = post["title"]
        subtitle = post["subtitle"]
        post_data.append(Post(id, body, title, subtitle))
    return post_data
