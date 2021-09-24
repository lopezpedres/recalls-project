from app.error_handler import ObjectNotFound
from flask import request, Blueprint
from flask_restful import Api, Resource
import jwt
import os

from .schemas import UserSchema
from .models import User
#Create a blueprint to connect to the app from another file that is not the app location
user_v1_bp=Blueprint('user_v1_bp',__name__)
#instance of the Schema
user_schema = UserSchema()
#Instance of the api with the schema
api =Api(user_v1_bp)

class UseriD(Resource):
    def get(self,user_id):
        user= User.get_by_id(user_id)
        if user is None:
            raise ObjectNotFound('The user does not exit')
        result = user_schema.dump(user)
        return result, 200



class login(Resource):
    def post(self):
        data = request.get_json()
        request_dict=user_schema.dump(data)
        user = User.get_by_email(email=request_dict['email'])
        if user is not None and user.check_password(request_dict['password']):
            pay_load = {
                'id': user.id,
                'email': user.email
                }
            resp = jwt.enconde(pay_load, os.getenv("SECRET_KEY"))
            user.session_token=resp
            user.save()
            return resp, 200
        else:
            raise ObjectNotFound('The user  or password are incorrect')

        



class UserNew(Resource):
    def post(self):
        data = request.get_json()
        request_dict = user_schema.load(data)
        user = User.simple_filter(email=request_dict['email'])
        if user:
            raise ObjectNotFound('There is a user with that email, try again')

        user = User(
            name = request_dict['name'],
            email = request_dict['email'],
            password = User.set_password(request_dict['password']),
            admin = request_dict['admin'])
        user.save()
        resp=user_schema.dump(user)
        return resp, 201
        

api.add_resource(UseriD, '/api/v1.0/<int:user_id>', endpoint='user_id')
api.add_resource(login, '/api/v1.0/login', endpoint='login')
api.add_resource(UserNew, '/api/v1.0/new_user', endpoint = 'user_new')
