import jwt
from flask import jsonify, request
from functools import wraps
from app.app import app

def check_token(func):
    @wraps(func)
    def wrapped(*args,**kwargs):
        token = request.arg.get('token')
        if not token:
            return jsonify('message: Missing Token'), 403
        try:    
            data = jwt.decode(token, app.config['SECRET_KEY'], 'HS256')
        except:
            return jsonify('message: Invalid Token'), 403
        return func(*args,**kwargs)
    return wrapped

