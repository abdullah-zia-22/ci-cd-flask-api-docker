"""Modules required for db connection"""
import mysql.connector


class DatabaseConnection():
    """class to handle data base query and connect to the mysql"""

    def __init__(self,host,databasename,charset,user,password,port):
        self.host = host
        self.databasename=databasename
        self.charset=charset
        self.user=user
        self.password=password
        self.port=port

    def connection(self):
        """function to get a fresh cursor and database object"""
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            port=self.port,
            password=self.password,
            charset=self.charset,
            database=self.databasename,
        )

        if db.is_connected():
            print("You're connected to database!")
        else:
            print("Error Connection!")
        cursor = db.cursor(buffered=True,dictionary=True)
        return cursor, db

    def close_connection(self, cursor, db):
        """close the connection using cursor and database object created"""
        cursor.close()
        db.close()
        if not db.is_connected():
            print("MySQL connection is closed")
        else:
            print("Connection is not closed Successfully!")
