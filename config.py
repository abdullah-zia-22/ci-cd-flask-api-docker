"""Modules required for configurations"""
from db import DatabaseConnection

HOST = "localhost"
DATABASENAME = "db_name"
USER = "username"
PASSWORD = "password"
CHARSET='utf8mb4'
PORT = 3306
MySqlDatabase = DatabaseConnection(HOST, DATABASENAME, CHARSET,USER, PASSWORD, PORT)
