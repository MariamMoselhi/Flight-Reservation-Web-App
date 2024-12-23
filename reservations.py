# from app.models.database_manager import DatabaseManager
import mysql.connector

class Reservations:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_reservations(self,user_id):
        query = """
        SELECT 
            Airline.airline_name AS Airline,
            Origin.airport_name AS Origin_Airport,
            Destination.airport_name AS Destination_Airport,
            User.username AS User_Name,
            Flight.departure_date as Departure_day,
            Flight.departure_time AS Departure_Time,
            Flight.arrival_date as arrival_day,
            Flight.arrival_time AS Arrival_Time,
            Ticket.seat_number AS Seat_Number
        FROM 
            Ticket
        JOIN 
            Flight ON Ticket.flight_id = Flight.flight_id
        JOIN 
            Airline ON Flight.airline_id = Airline.airline_id
        JOIN 
            Airport AS Origin ON Flight.origin_airport_id = Origin.airport_id
        JOIN 
            Airport AS Destination ON Flight.destination_airport_id = Destination.airport_id
        JOIN 
            User ON Ticket.user_id = User.user_id
        WHERE User.user_id=%s;
        """
        try:
            name = (user_id,)
            # self.db_manager.mycursor.execute(query, name)
            self.db_manager.mycursor.execute(query, name)
            result = self.db_manager.fetch_all()
            # result = self.fetch_all()
        except Exception as e:
            print(f"Error: {e}")
            result = None
        return result

    