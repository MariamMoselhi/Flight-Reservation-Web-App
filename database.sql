CREATE DATABASE App;
USE App;

CREATE TABLE Airport (
    airport_id INT AUTO_INCREMENT PRIMARY KEY,
    airport_name VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL
);

CREATE TABLE Airline (
    airline_id INT AUTO_INCREMENT PRIMARY KEY,
    airline_name VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL
);
CREATE TABLE Flight (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    departure_date DATE NOT NULL,
    arrival_date DATE NOT NULL,
	departure_time TIME NOT NULL,
    arrival_time TIME NOT NULL,
    duration TIME NOT NULL,
    available_seats INT NOT NULL,
    airline_id INT NOT NULL,
    origin_airport_id INT NOT NULL,
    destination_airport_id INT NOT NULL,
    FOREIGN KEY (airline_id) REFERENCES Airline(airline_id),
    FOREIGN KEY (origin_airport_id) REFERENCES Airport(airport_id),
    FOREIGN KEY (destination_airport_id) REFERENCES Airport(airport_id)
);

CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    passport_number VARCHAR(15) NOT NULL UNIQUE
);

CREATE TABLE Ticket (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    flight_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    seat_number VARCHAR(10) NOT NULL,
    class ENUM('Economy', 'Business', 'First') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (flight_id) REFERENCES Flight(flight_id)
);

CREATE TABLE Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    ticket_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
   --  transaction_time DATETIME NOT NULL,
    FOREIGN KEY (ticket_id) REFERENCES Ticket(ticket_id)
);


INSERT INTO Airport (airport_name, country, city) VALUES
('Hartsfield-Jackson Atlanta International Airport', 'USA', 'Atlanta'),
('Beijing Capital International Airport', 'China', 'Beijing'),
('Dubai International Airport', 'UAE', 'Dubai'),
('Tokyo Haneda Airport', 'Japan', 'Tokyo'),
('Heathrow Airport', 'UK', 'London');


INSERT INTO Airline (airline_name, country) VALUES
('Delta Airlines', 'USA'),
('Air China', 'China'),
('Emirates', 'UAE'),
('Japan Airlines', 'Japan'),
('British Airways', 'UK');


INSERT INTO Flight (departure_date, arrival_date, departure_time, arrival_time, duration, available_seats, airline_id, origin_airport_id, destination_airport_id) VALUES
('2024-12-01', '2024-12-01', '08:00:00', '12:00:00', '04:00:00', 200, 1, 1, 3),
('2024-12-02', '2024-12-02', '14:00:00', '22:00:00', '08:00:00', 150, 2, 2, 4),
('2024-12-03', '2024-12-04', '23:00:00', '03:00:00', '04:00:00', 300, 3, 3, 5),
('2024-12-04', '2024-12-05', '09:00:00', '16:00:00', '07:00:00', 250, 4, 4, 1),
('2024-12-05', '2024-12-06', '18:00:00', '23:30:00', '05:30:00', 180, 5, 5, 2);


INSERT INTO User (username, email, password, passport_number) VALUES
('john_doe', 'john.doe@example.com', 'hashed_password_123', 'A12345678'),
('jane_smith', 'jane.smith@example.com', 'hashed_password_456', 'B87654321'),
('aviator_99', 'aviator99@example.com', 'hashed_password_789', 'C23456789'),
('travel_guru', 'guru.travel@example.com', 'hashed_password_abc', 'D98765432'),
('jet_setter', 'jet.setter@example.com', 'hashed_password_xyz', 'E34567890');

INSERT INTO User (username, email, password, passport_number) VALUES
('khaled', 'khaled123@yahoo.com', '12345', 'A12345672');

INSERT INTO Ticket (user_id, flight_id, price, seat_number, class) VALUES
(1, 1, 350.00, '12A', 'Economy'),
(2, 2, 1200.00, '1B', 'Business'),
(3, 3, 700.00, '15C', 'Economy'),
(4, 4, 500.00, '8D', 'Economy'),
(5, 5, 2000.00, '2A', 'First');


INSERT INTO Payment (ticket_id, price) VALUES
(1, 350.00),
(2, 1200.00),
(3, 700.00),
(4, 500.00),
(5, 2000.00);
select * from Payment;
select * from Flight;
select * from Airline;
select * from user; 
select * from Ticket;