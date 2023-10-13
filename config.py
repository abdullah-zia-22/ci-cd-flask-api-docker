"""Modules required for configurations"""
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from api import app
from db import DatabaseConnection

app.secret_key = "super-secret"
app.config['JSON_SORT_KEYS']=False

# CORS
CORS(app, resources={r"/*": {"origins": "*"}})

HOST = "localhost"
DATABASENAME = "db_name"
USER = "username"
PASSWORD = "password"
CHARSET='utf8mb4'
PORT = 3306
MySqlDatabase = DatabaseConnection(HOST, DATABASENAME, CHARSET,USER, PASSWORD, PORT)

# JWT Authentication
app.config['JWT_SECRET_KEY'] = app.secret_key  # This can be changed
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)
blacklist = set()
