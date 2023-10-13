"""Modules required for API"""
from flask_restful import Api
#API ROUTES IMPORT
from app import app
from user import Login

#ROUTES
api = Api(app)
api.add_resource(Login, "/Login")
