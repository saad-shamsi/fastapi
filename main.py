from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Blog(BaseModel):
    title: str
    body: str
    published: bool = True


app = FastAPI()


@app.get("/")
def index(limit: int = 10, published: bool = True, sort: str | None = None):
    if published:
        return {"data": f"{limit} publishded blogs from db"}

    else:
        return {"data": f"{limit} blogs from db"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


@app.get("/blog/{id}")
def blog(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def blog_comments(id):
    return {"data": {"1", "2"}}


@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog is created with title as {request.title}"}


# if __name__ == "__main__":

#     uvicorn.run(app, host="127.0.0.1", port=9000)
