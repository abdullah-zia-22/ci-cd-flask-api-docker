import math
from config import MySqlDatabase,mail,regex,jwt,blacklist,react_route
from flask import jsonify,session,render_template,Response,make_response,stream_with_context
from flask_restful import Resource, reqparse,request,abort
import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (create_access_token,
create_refresh_token,
get_jwt_identity)
from utils import jwt_required,role


# ROUTES DEFINITIONS
# Request arguments for Login
login_args = reqparse.RequestParser()
login_args.add_argument("email", type=str, help="Email for Login", required=True)
login_args.add_argument("password", type=str, help="Password for Login", required=True)

class Login(Resource):
    def post(self):
        args = login_args.parse_args()
        #username and password checks
        email = args['email']
        if(email[0].isdigit()):
            message = "Email should not start with a number"
            abort(http_status_code=406,message=message)

        if (" " in email):
            message = "Email should not contain any space"
            abort(http_status_code=406,message=message)

        password = args['password']

        #retreiving hashed password from db to compare
        cursor,db=MySqlDatabase.connection()
        cursor.execute("SELECT id,password from admin where email=%s or username=%s", (email,email))
        admin=cursor.fetchone()
        if not admin:
            message = "Incorrect Email or Password. Try Again!"
            abort(http_status_code=404,message=message)

        

        if check_password_hash(admin['password'], password):
            #returning access, refresh token
            expires = dt.timedelta(minutes=30)
            access_token = create_access_token(identity=str(admin['id']),additional_claims={"role": "Admin"},expires_delta=expires)
            refresh_token = create_refresh_token(identity=str(admin['id']),additional_claims={"role": "Admin"})
            MySqlDatabase.close_connection(cursor,db)
            return jsonify({"status":200,'access_token': access_token,"refresh_token":refresh_token})

        else:
            message = "Incorrect Email or Password. Try Again!"
            MySqlDatabase.close_connection(cursor,db)
            abort(http_status_code=404,message=message)

