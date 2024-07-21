from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # This sets true as default value if the user doesn't provide a value
    rating: Optional[int] = None


my_posts = [{"title": "title  of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


@app.get("/")  # FastAPI decorator takes the REST method & the path
def root():
    return {"message": "hello world"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"post_detail": post}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(3, 10000000)
    my_posts.append(post_dict)
    print(post.title)
    print(post.dict())  # To convert pydantic schema to dictionary
    return {"data": post_dict}

