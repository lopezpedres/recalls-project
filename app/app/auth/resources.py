from app.error_handler import ObjectNotFound
from flask import request, Blueprint
from flask_restful import Api, Resource

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



class UserCheck(Resource):
    def get(self, email):
        user = User.simple_filter(email=email) #Is not returning the user
        if user is None:
            raise ObjectNotFound('The user does not exit')
        result = user_schema.dump(user)
        return result, 200



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
api.add_resource(UserCheck, '/api/v1.0/email/<string:email>', endpoint='user_email')
api.add_resource(UserNew, '/api/v1.0/new_user', endpoint = 'user_new')
