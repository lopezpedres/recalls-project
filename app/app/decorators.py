import jwt
from flask import jsonify, request, abort, make_response
from functools import wraps
import os

def check_token(func):
    @wraps(func)
    def wrapped(*args,**kwargs):
        # Bearer <token>
        print('Checking token')
        #token = request.headers['Authorization'] #Uncomment if needed
        token = request.args.get("token") 
        print(token)
        if token is None or token.strip() == "Bearer" or token.strip() == "":
            return make_response({'msg': 'No token'},403)
        try:    
            #token = token.split(" ")[1] #Uncomment if Bearer
            data = jwt.decode(token, os.getenv('SECRET_KEY'), 'HS256')
        except:
            return make_response({'msg': 'Invalid Token'}, 403)
        return func(*args,**kwargs)
    return wrapped

