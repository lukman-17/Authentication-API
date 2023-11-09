import time
from typing import Dict
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# funtion returns the generated token (JWTs)
def token_response(token: str):
    return {
         " access token" : token 
    }
#funtion used for singing the JWT String 
def signJWT(userID :str):
    payload = { 
        "userID":userID,
        "expiry" : time.time() + 600
    }
    token=jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token :str):
    try:
         decode_token=jwt.decode(token,JWT_SECRET,algorithm=JWT_ALGORITHM)
         return decode_token if decode_token['expires']>=time.time() else None
    except:
        return{}