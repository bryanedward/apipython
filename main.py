from random import randrange
from fastapi import FastAPI, Response
from controllers.post import find_post
from models.model import Post
from mocks.data import posts
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World on"}


@app.post('/createpost')
def create_post(post: Post):
    new_post = post.dict()
    new_post['id'] = randrange(0, 50000)
    posts.append(new_post)
    return {"response": posts}


@app.get('/findpost/{id}')
def get_post(id: int, response: Response):
    result = find_post(id)
    if not result:
        response.status_code = 404
        return {"message": f"not exist {id} in the database"}
    return result
