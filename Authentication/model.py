from pydantic import BaseModel,Field,EmailStr
from fastapi import FastAPI
import json
app=FastAPI()

class PostSchema(BaseModel):
    id:int=Field(default=None)
    title:str=Field(default=None)
    content:str=Field(default=None)
    class Config:
        schema_extra = {
            "post_demo": { 
                "title": "language",
                "content":"something about cs languages"
            }
        }

class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema={
            "user_demo": {
                "name" : "lukman",
                "email" : "jhondoe@gmail.com",
                "password": "123"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema={
            "user_demo": {
                "email" : "jhondoe@gmail.com",
                "password": "123"
            }
        }
       