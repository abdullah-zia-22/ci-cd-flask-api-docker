"""Modules required for configurations"""
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from api import app
from db import DatabaseConnection

HOST = "localhost"
DATABASENAME = "db_name"
USER = "username"
PASSWORD = "password"
CHARSET='utf8mb4'
PORT = 3306
MySqlDatabase = DatabaseConnection(HOST, DATABASENAME, CHARSET,USER, PASSWORD, PORT)

app.secret_key = "super-secret"
app.config['JSON_SORT_KEYS']=False

# CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# Make a regular expression
# for validating an Email
REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Mail config
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

#react routes for reseting password email to redirect to page
REACT_ROUTE="http://localhost:3000"
FLASK_ROUTE="http://127.0.0.1:5000"



# JWT Authentication
app.config['JWT_SECRET_KEY'] = app.secret_key  # This can be changed
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)
blacklist = set()
