#imports
from flask import Flask
from flask_restful import Api

#Flask app, api creation

app = Flask(__name__)
api = Api(app)


#API ROUTES IMPORT
from user import *


#ROUTES

api.add_resource(Login, "/Login")



