from fastapi import FastAPI,Body,Depends
from model import PostSchema
from model import PostSchema,UserSchema,UserLoginSchema
from jwt_handler import signJWT
from jwt_bearer import JWTBearer
app=FastAPI()
posts = [
     {
          "id" : 1,
          "title" : "python",
          "text": " python is fast and very popular language "
     },
     {
          "id" : 2,
          "title" : "java",
          "text": " java is easy to learn and secure language "
     },
     {
          "id" : 3,
          "title" : "javascript",
          "text": " javascript has multiple frameworks to use "
     }
]
users=[]
# Get for testing 


@app.get("/",tags=["test"])
def greet():
     return {"Hello":"world!"}

#get single posts
@app.get("/posts",tags=["posts"]) 
def get_posts():
     return {"data":posts}

# Get single posts{id}
@app.get("/posts/{id}",tags=["posts"])
def get_one_posts(id : int):
     if id>len(posts):
          return {
               "error":"Post with this id does not exist!"
          }
     for post in posts:
          if post["id"]==id:
               return {
                    "data":post
               }
# post a blog post]A handler for creating a post]
@app.post("/posts",dependencies=[Depends(JWTBearer())],tags=["posts"])
def add_post(post:PostSchema):
     post.id=len(posts)+1
     posts.append(post.dict())
     return{
          "info":"post Added"
     }

# user signup [create new user]
@app.post("user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
           users.append(user)
           return signJWT(user.email)

def check_user(data:UserLoginSchema):
      for user in users:
            if user.email == data.email and user.password == data.password:
                  return True
            return False
  
@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
      if check_user(user):
            return signJWT(user.email)     
      else :
            return {
                  "error":"invalid login details"
            }