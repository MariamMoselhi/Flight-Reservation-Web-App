import mysql.connector
from datetime import datetime

from DataBase import DatabaseManager  # Import the DatabaseManager class
db_manager = DatabaseManager(host="localhost", user="root", password="1234", database="App")

# class Book:
#     def __init__(self, db_connection):
#     # Use the existing DatabaseManager object properly
#          self.db_manager = db_connection

#     def available_seats(self, flight_id):
#         sql_query = "SELECT available_seats FROM flight WHERE flight_id=%s"
#         self.db_manager.mycursor.execute(sql_query, (flight_id,))
#         result = self.db_manager.mycursor.fetchall()
#         self.db_manager.conn.commit()
#         if len(result) == 0:
#             return None
#         return result[0][0]

#     def update_seats(self, flight_id):
#         sql_query = "UPDATE flight SET available_seats = available_seats - 1 WHERE flight_id=%s;"
#         self.db_manager.mycursor.execute(sql_query, (flight_id,))
#         self.db_manager.conn.commit()

#     def ticket_price(self, flight_id):
#         sql_query = "SELECT price FROM ticket WHERE flight_id=%s"
#         self.db_manager.mycursor.execute(sql_query, (flight_id,))
#         result = self.db_manager.mycursor.fetchall()
#         self.db_manager.conn.commit()
#         if len(result) == 0:
#             return None
#         return result[0][0]

#     def add_ticket(self, user_id, flight_id, price):
#         class_name = "First"
#         seat_number = "10B"
#         query = "INSERT INTO ticket (user_id, flight_id, price, seat_number, class) VALUES (%s, %s, %s, %s, %s);"
#         values = (user_id, flight_id, price, seat_number, class_name)
#         self.db_manager.mycursor.execute(query, values)
#         self.db_manager.conn.commit()
        
#     def flights(self, from_airport, to_airport, departure_date):
#         formatted_date = datetime.strptime(departure_date, "%Y-%m-%d").date()
        
#         data = (to_airport, from_airport, formatted_date)
#         query = """
#         SELECT DISTINCT Flight.flight_id, Airline.airline_name, Flight.available_seats, Flight.departure_time,
#                Flight.arrival_time, Ticket.price, OriginAirport.airport_name AS origin_airport_name,
#                DestinationAirport.airport_name AS destination_airport_name
#         FROM Ticket
#         JOIN Flight ON Ticket.flight_id = Flight.flight_id
#         JOIN Airline ON Flight.airline_id = Airline.airline_id
#         JOIN Airport AS OriginAirport ON Flight.origin_airport_id = OriginAirport.airport_id
#         JOIN Airport AS DestinationAirport ON Flight.destination_airport_id = DestinationAirport.airport_id
#         WHERE DestinationAirport.airport_name=%s 
#           AND OriginAirport.airport_name=%s 
#           AND Flight.departure_date=%s;
#         """
#         self.db_manager.mycursor.execute(query, data)
#         result = self.db_manager.mycursor.fetchall()
#         # self.db_manager.conn.commit()
#         return result


class Book:
    def __init__(self, db_connection):  # Corrected the method name to __init__
        # Use the existing DatabaseManager object properly
        self.db_manager = db_connection

    def available_seats(self, flight_id):
        sql_query = "SELECT available_seats FROM flight WHERE flight_id=%s"
        self.db_manager.mycursor.execute(sql_query, (flight_id,))
        result = self.db_manager.mycursor.fetchall()
        self.db_manager.conn.commit()
        if len(result) == 0:
            return None
        return result[0][0]

    def update_seats(self, flight_id):
        sql_query = "UPDATE flight SET available_seats = available_seats - 1 WHERE flight_id=%s;"
        self.db_manager.mycursor.execute(sql_query, (flight_id,))
        self.db_manager.conn.commit()

    def ticket_price(self, flight_id):
        sql_query = "SELECT price FROM ticket WHERE flight_id=%s"
        self.db_manager.mycursor.execute(sql_query, (flight_id,))
        result = self.db_manager.mycursor.fetchall()
        self.db_manager.conn.commit()
        if len(result) == 0:
            return None
        return result[0][0]

    def add_ticket(self, user_id, flight_id, price):
        class_name = "First"
        test_seat = (flight_id,)
        query = "SELECT ticket_id FROM ticket WHERE flight_id = %s"
        self.db_manager.mycursor.execute(query, test_seat)
        result = self.db_manager.mycursor.fetchall()

        last_element = result[-1]  # This will give you the last tuple
        last_ticket = last_element[0]  # Assuming ticket_id is the first column in the result

        if last_ticket < 30:
            seat_number = str(last_ticket) + "B"
        elif 29 < last_ticket < 60:
            seat_number = str(last_ticket) + "C"
        else:
            seat_number = str(last_ticket) + "D"

        query = "INSERT INTO ticket (user_id, flight_id, price, seat_number, class) VALUES (%s, %s, %s, %s, %s);"
        values = (user_id, flight_id, price, seat_number, class_name)
        self.db_manager.mycursor.execute(query, values)
        self.db_manager.conn.commit()

    def flights(self, from_airport, to_airport, departure_date):
        formatted_date = datetime.strptime(departure_date, "%Y-%m-%d").date()
        data = (to_airport, from_airport, formatted_date)
        query = """
        SELECT DISTINCT Flight.flight_id, Airline.airline_name, Flight.available_seats, Flight.departure_time,
               Flight.arrival_time, Ticket.price, OriginAirport.airport_name AS origin_airport_name,
               DestinationAirport.airport_name AS destination_airport_name
        FROM Ticket
        JOIN Flight ON Ticket.flight_id = Flight.flight_id
        JOIN Airline ON Flight.airline_id = Airline.airline_id
        JOIN Airport AS OriginAirport ON Flight.origin_airport_id = OriginAirport.airport_id
        JOIN Airport AS DestinationAirport ON Flight.destination_airport_id = DestinationAirport.airport_id
        WHERE DestinationAirport.airport_name=%s 
          AND OriginAirport.airport_name=%s 
          AND Flight.departure_date=%s;
        """
        self.db_manager.mycursor.execute(query, data)
        result = self.db_manager.mycursor.fetchall()
        return result



