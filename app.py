from flask import Flask, render_template, jsonify, request, abort, redirect, session, flash
import mysql.connector
from flask_bcrypt import Bcrypt
from datetime import datetime
import re #regular exp

from DataBase import DatabaseManager  # Import the DatabaseManager class
db_manager = DatabaseManager(host="localhost", user="root", password="1234", database="App")

from login import Login  # Import Login class
login = Login(db_manager)
from reservations import Reservations  # Import Reservations class
reservation = Reservations(db_manager)
from signup import Signup  # Import Signup class
signups = Signup(db_manager)
from book import Book  # Import the Book class
books = Book(db_manager)

bcrypt = Bcrypt()

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key'



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


# -----------------login----------------------------------------


@app.route("/registration")
def registration():
    return render_template('registration.html')

@app.route('/registration', methods=['POST'])
def my_form_post():
    email = request.form['email']
    password = request.form['password']
    check = login.check_user(email, password)
    if check:
        #return redirect('/book')
        flash("You have Logged in !","success")  # Flash a success message
        return redirect('/')
    else:
        return redirect('/registration')



# -------------------------signup-------------------------

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/signup", methods=['POST'])
def signup_post():
    username = request.form['username']
    passport_number = request.form['passport_number']
    email = request.form['email']
    password = request.form['password']
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    if signups.validate_passport_id(passport_number) and signups.validate_email(email) and signups.validate_username(username):
        signups.insert_user(username, passport_number, email, hashed_password)
        return redirect('/registration')
    else:
        flash("Wrong data !","danger")  # Flash a success message
        return redirect('/signup')
# -------------------------book-------------------------
@app.route("/book")
def book():
    return render_template('book.html')

@app.route("/book", methods=['POST'])
def search():
    from_airport = request.form['from-airport']
    to_airport = request.form['to-airport']
    departure_date = request.form['departure']
    # formatted_date = datetime.strptime(departure_date, "%Y-%m-%d").date()
    # data = (to_airport, from_airport, formatted_date)
    # Call the flights function to get the flight data
    result = books.flights(from_airport, to_airport, departure_date)
    # result = books.flights("Beijing Capital International Airport", "Tokyo Haneda Airport", "2024-12-02")

    return render_template('availableFlights.html', flights=result)

@app.route("/availableFlights", methods=['POST'])
def availableFlights():
    return render_template('availableFlights.html', flights=None)

@app.route("/availableFlights/<id>")
def reserve(id):
    # Check if the user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        open_seats=books.available_seats(id)
        if (open_seats > 0):
            price=books.ticket_price(id)
            books.add_ticket(user_id,id,price)
            books.update_seats(id)
            #return "<h1 style='color: green;'>Done successfully</h1>", 200
            #flash("This registration!", "success")  # Flash a success message
            return redirect('/reservations')
            
        else:
            return  "<h1 style='color: red;'>No Available Seats</h1>", 200
    else:
        return redirect('/registration')  # Redirect to registration page if not logged in



# --------------------------------------------------reservation------------------------------------------------
# @app.route("/reservations")
# def reservations():
#     # Check if the user is logged in
#     if 'user_id' in session:
#         user_id = session['user_id']
#         result = reservation.get_reservations(user_id)
#         return render_template('reservations.html',tickets=result)
#         #return "<h1 style='color: green;'>"+str(user_id)+"</h1>", 200
#     else:
#         return redirect('/registration')  # Redirect to registration page if not logged in


@app.route("/reservations")
def reservations():
    # Check if the user is logged in
    if 'user_id' in session:
        user_id = session['user_id']
        result = reservation.get_reservations(user_id)
        if result is None:
            result = []  # Ensure result is always iterable
        return render_template('reservations.html', tickets=result)
    else:
        return redirect('/registration')  # Redirect to registration page if not logged in



#   APIs
@app.route("/api/reservations")
def reservations_json():
    if 'user_id' in session:
        user_id = session['user_id']
        result = reservation.get_reservations(user_id)
        
    return jsonify(str(result))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)