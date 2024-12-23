import re
from flask_bcrypt import Bcrypt
import mysql.connector

bcrypt = Bcrypt()

class Signup:
    def __init__(self, db_connection):
    # Use the existing DatabaseManager object properly
         self.db_manager = db_connection

    def insert_user(self, username, passport_number, email, password):
        query = "INSERT INTO User (email, username, password, passport_number) VALUES (%s, %s, %s, %s);"
        values = (email, username, password, passport_number)
        self.db_manager.mycursor.execute(query, values)
        self.db_manager.conn.commit()

    # def validate_email(self, email):
    #     pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}$'
    #     return re.match(pattern, email) is not None
    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}$'
        email_name = (email,)
        query = "select email from User where email=%s"
        self.db_manager.mycursor.execute(query, email_name)
        result = self.db_manager.mycursor.fetchall()
        # return re.match(pattern, email) is not None
        return (re.match(pattern, email) is not None ) and (len(result) == 0)



    def validate_username(self, username):
        pattern = r'^[a-zA-Z0-9_]{3,15}$'

        user_name = (username,)
        query = "select username from User where username=%s"
        self.db_manager.mycursor.execute(query, user_name)
        result = self.db_manager.mycursor.fetchall()
        return (re.match(pattern, username) is not None) and (len(result)==0)



    # def validate_passport_id(self, passport_id):
    #     pattern = r'^[A-Z0-9]{8,9}$'
    #     return re.match(pattern, passport_id) is not None
    def validate_passport_id(self, passport_id):
        pattern = r'^[A-Z0-9]{8,9}$'
        passpor = (passport_id,)
        query = "select passport_number from User where passport_number=%s"
        self.db_manager.mycursor.execute(query, passpor)
        result = self.db_manager.mycursor.fetchall()
        # return re.match(pattern, passport_id) is not None
        return (re.match(pattern, passport_id) is not None) and (len(result) == 0)