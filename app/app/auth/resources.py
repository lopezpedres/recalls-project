from app.decorators import check_token
from flask.json import jsonify
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

class UserAll(Resource):
    def get(self):
        users= User.get_all()
        print(users)
        if len(users) == 0:
            raise ObjectNotFound('There are no Users')
        result = user_schema.dump(users, many=True)
        return result, 200




class login(Resource):
    def post(self):
        data = request.get_json()
        request_dict=user_schema.dump(data)
        user = User.get_by_email(request_dict['email'])
        if user is None:
            raise ObjectNotFound('The user  or password are incorrect')
        if user.check_password(request_dict['password']): 
            pay_load = {
                'id': user.id,
                'email': user.email
                }
            token = jwt.encode(payload=pay_load, key=os.getenv('SECRET_KEY'))
            user.session_token=token
            user.save()
            resp=token
            return resp, 200
        else:
            raise ObjectNotFound('The user does not exit')
    

        

class UserNew(Resource):
    #@check_token
    def put(self):
        data = request.get_json()
        request_dict = user_schema.load(data)
        user = User.get_by_email(email=request_dict['email'])

        if user:
            raise ObjectNotFound('There is a user with that email, try again')

        user = User(
            name = request_dict['name'],
            email = request_dict['email'],
            admin = request_dict['admin'])
        user.set_password(request_dict.get('password'))
        user.save()
        resp=user_schema.dump(user)
        return resp, 201

        

api.add_resource(UseriD, '/api/v1/users/<int:user_id>', endpoint='get-user')
api.add_resource(UserAll, '/api/v1/users', endpoint='all-users')
api.add_resource(login, '/api/v1/login', endpoint='login')
api.add_resource(UserNew, '/api/v1/users', endpoint = 'new-user')
