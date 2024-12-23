import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="App")
        self.mycursor = self.conn.cursor()

    def execute_query(self, query, values):
        self.mycursor.execute(query, values)
        self.conn.commit()

    def fetch_all(self):
        return self.mycursor.fetchall()

    def close_connection(self):
        self.mycursor.close()
        self.conn.close()
