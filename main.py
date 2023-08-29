from fastapi.exceptions import HTTPException
from exceptions import StoryException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from router import blog_get, blog_post, user, article, product
from auth import authentication
from db import models
from db.database import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index():
    return {"message": "Hello World!"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={"detail": exc.name})


# Custom exception handler
# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: HTTPException):
#     return PlainTextResponse(str(exc), status_code=400)

# Database creation. If database already exists, it will not recreate it.
# It is only created when the file is not there.
models.Base.metadata.create_all(engine)

origins = ["http://localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)