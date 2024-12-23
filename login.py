from flask import session
from flask_bcrypt import Bcrypt
from flask import abort
import mysql.connector

bcrypt = Bcrypt()

class Login:
    # def __init__(self, db_connection):
    #     self.conn = db_connection
    #     self.mycursor = self.conn.cursor()
    def __init__(self, db_connection):
    # Use the existing DatabaseManager object properly
         self.db_manager = db_connection

    def check_user(self,email_name, password):
        email = (email_name,)
        query = "select password, user_id from User where email=%s"
        self.db_manager.mycursor.execute(query, email)
        result = self.db_manager.mycursor.fetchall()
        try:
            if bcrypt.check_password_hash(result[0][0], password):
            # Store user_id in session
              session['user_id'] = result[0][1]
              return True
            else:
                return False
        except IndexError:
              abort(401)
    