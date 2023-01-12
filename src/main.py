from fastapi import FastAPI, status, HTTPException
from controllers.post import get_posts, create, find_post, find_index
from models.model import Post
from mocks.data import posts
app = FastAPI()


@app.get("/")
async def root():
    results = get_posts()
    return {"data": results}


@app.post('/createpost', status_code=status.HTTP_201_CREATED)
def createpost(post: Post):
    results = create(post)
    print(results)


@app.get('/findpost/{id}')
def get_post(id: int):
    result = find_post(id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the id {id} not exists")
    return result


@app.delete('/deletepost/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    result = find_index(id)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='not exits')
    posts.pop(result)
    return {posts}


@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    index = find_index(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post_dict = post.dict()
    post_dict['id'] = id
    posts[index] = post_dict
    return {"data": posts}
