"""Modules required for user module"""
import datetime as dt
from flask import jsonify
from flask_restful import Resource, reqparse,abort
from werkzeug.security import check_password_hash
from flask_jwt_extended import (create_access_token,
create_refresh_token)
from config import MySqlDatabase


# ROUTES DEFINITIONS
# Request arguments for Login
login_args = reqparse.RequestParser()
login_args.add_argument("email", type=str, help="Email for Login", required=True)
login_args.add_argument("password", type=str, help="Password for Login", required=True)

class Login(Resource):
    """class for Login route"""
    def post(self):
        """login post route"""
        args = login_args.parse_args()
        #username and password checks
        email = args['email']
        if email[0].isdigit():
            message = "Email should not start with a number"
            return abort(http_status_code=406,message=message)

        if " " in email:
            message = "Email should not contain any space"
            return abort(http_status_code=406,message=message)

        password = args['password']

        #retreiving hashed password from db to compare
        cursor,db=MySqlDatabase.connection()
        cursor.execute("SELECT id,password from admin where email=%s or username=%s", (email,email))
        admin=cursor.fetchone()
        if not admin:
            message = "Incorrect Email or Password. Try Again!"
            return abort(http_status_code=404,message=message)

        if check_password_hash(admin['password'], password):
            #returning access, refresh token
            expires = dt.timedelta(minutes=30)
            access_token = create_access_token(identity=str(admin['id']),
            additional_claims={"role": "Admin"},expires_delta=expires)
            refresh_token = create_refresh_token(identity=str(admin['id']),
            additional_claims={"role": "Admin"})
            MySqlDatabase.close_connection(cursor,db)
            return jsonify({"status":200,'access_token':
            access_token,"refresh_token":refresh_token})

        message = "Incorrect Email or Password. Try Again!"
        MySqlDatabase.close_connection(cursor,db)
        return abort(http_status_code=404,message=message)
