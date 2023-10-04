from api import app
import os
from flask_cors import CORS
from flask_mail import Mail
from db import DatabaseConnection
from flask_jwt_extended import JWTManager

host = "localhost"
databasename = "db_name"
user = "username"
password = "password"
charset='utf8mb4'
port = 3306
MySqlDatabase = DatabaseConnection(host, databasename, charset,user, password, port)

app.secret_key = "super-secret"
app.config['JSON_SORT_KEYS']=False

# CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Mail config
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

#react routes for reseting password email to redirect to page
react_route="http://localhost:3000"
flask_route="http://127.0.0.1:5000"


#  Following are My Personal credentials
app.config['MAIL_USERNAME'] = 'developercodeaza@gmail.com'
app.config['MAIL_PASSWORD'] = 'zsnsvlvninoizjzs'
mail = Mail(app)


# JWT Authentication
app.config['JWT_SECRET_KEY'] = app.secret_key  # This can be changed
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)
blacklist = set()


# file management
app.config["FILES"] = os.path.join(app.root_path, "static/uploads")
