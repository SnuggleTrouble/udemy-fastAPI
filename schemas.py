from typing import List
from pydantic import BaseModel


# Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


# UserBase. The type of data that we receive from the user.
# aka Data from user.
class UserBase(BaseModel):
    username: str
    email: str
    password: str


# UserDisplay. The type of data we provide to the user.
# aka Response to user.
class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []

    class Config:
        orm_mode = True


# ------------------------------------------------------------------------


# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


# We receive this from the user when creating an article
class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


# Data structure to send to the user once we have created
# and have received the article
class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        orm_mode = True
