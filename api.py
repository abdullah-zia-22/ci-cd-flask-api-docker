"""Modules required for API"""
from flask import Flask
from flask_restful import Api
#API ROUTES IMPORT
from user import Login
#Flask app, api creation
app = Flask(__name__)
api = Api(app)
#ROUTES
api.add_resource(Login, "/Login")
