"""Modules required for API"""
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
#API ROUTES IMPORT
from user import Login
#Flask app, api creation
app = Flask(__name__)
app.secret_key = "super-secret"
app.config['JSON_SORT_KEYS']=False
# CORS
CORS(app, resources={r"/*": {"origins": "*"}})
# JWT Authentication
app.config['JWT_SECRET_KEY'] = app.secret_key  # This can be changed
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)
blacklist = set()
#ROUTES
api = Api(app)
api.add_resource(Login, "/Login")
