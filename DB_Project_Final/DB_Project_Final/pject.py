#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 20:08:36 2019

@author: robertonoel, nealshu
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:56:53 2019

@author: robertonoel, nealshu
"""

#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import datetime

import hashlib 
#Initialize the app from Flask
app = Flask(__name__, template_folder='C:\\Users\\14297\\Desktop\\DB_Project_Final\\DB_Project_Final\\')
app.static_folder = 'C:\\Users\\14297\\Desktop\\DB_Project_Final\\DB_Project_Final\\css'

#Configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='NewDatabase',
                       charset='utf8mb4',
                       port = 3306,
                       cursorclass=pymysql.cursors.DictCursor)

#Define a route to hello function
@app.route('/')
def search():
	return render_template('index.html')
@app.route('/searchAuth', methods=['GET', 'POST'])
def searchAuth():
	#grabs information from the forms
    session['flight_type'] = request.form['flight-type']
    session['departs'] = request.form['departs']
    session['arrives'] = request.form['arrives']
    session['depdate'] = request.form['depdate']
    session['retdate'] = request.form['retdate']
    session['searchby'] = request.form['search-by']
    
    print(session['flight_type'])
    print(session['departs'])
    print(session['arrives'])
    print(session['depdate'])
    print(session['retdate'])
    return redirect(url_for('results'))

@app.route('/results')
def results():
    
    flight_type = session['flight_type']
    departs = session['departs']
    arrives = session['arrives']
    depdate = session['depdate']
    retdate = session['retdate']
    searchby = session['searchby']
    cursor = conn.cursor();
    
    if searchby == "airport":
            
        if flight_type == "roundtrip":
            query = """SELECT airline_name, flight.flight_no, departure_date_time, departs_from, arrival_date_time, 
            arrives_from, real_price, A.city as departure_city, B.city as arrival_city
            FROM pricing, flight, airport as A, airport as B where
            pricing.flight_no = flight.flight_no and
            departs_from = A.name and arrives_from = B.name and departure_date_time > Now() and (
            (departure_date_time like %s and departs_from = %s and arrives_from = %s) or 
            (departure_date_time like %s and departs_from = %s and arrives_from = %s and departure_date_time > %s))"""
            print(query % ((depdate + "%"), departs, arrives, (retdate + "%"), arrives, departs, depdate))
            cursor.execute(query, ((depdate + "%"), departs, arrives, (retdate + "%"), arrives, departs, depdate))
        else:
            query = """SELECT airline_name, flight.flight_no, departure_date_time, departs_from, arrival_date_time, 
            arrives_from, real_price, A.city as departure_city, B.city as arrival_city
            FROM pricing, flight, airport as A, airport as B where
            pricing.flight_no = flight.flight_no and
            departs_from = A.name and arrives_from = B.name and departure_date_time > Now() and 
            departure_date_time like %s and departs_from = %s and arrives_from = %s"""
            cursor.execute(query, ((depdate + "%"), departs, arrives))
    else:
        
        if flight_type == "roundtrip":
            query = """SELECT airline_name, flight.flight_no, departure_date_time, departs_from, arrival_date_time, 
            arrives_from, real_price, A.city as departure_city, B.city as arrival_city
            FROM pricing, flight, airport as A, airport as B where
            pricing.flight_no = flight.flight_no and
            departs_from = A.name and arrives_from = B.name and departure_date_time > Now() and (
            (departure_date_time like %s and A.city = %s and B.city = %s) or 
            (departure_date_time like %s and A.city = %s and B.city = %s and departure_date_time > %s))"""
            print(query % ((depdate + "%"), departs, arrives, (retdate + "%"), arrives, departs, depdate))
            cursor.execute(query, ((depdate + "%"), departs, arrives, (retdate + "%"), arrives, departs, depdate))
        else:
            query = """SELECT airline_name, flight.flight_no, departure_date_time, departs_from, arrival_date_time, 
            arrives_from, real_price, A.city as departure_city, B.city as arrival_city
            FROM pricing, flight, airport as A, airport as B where
            pricing.flight_no = flight.flight_no and
            departs_from = A.name and arrives_from = B.name and departure_date_time > Now() and 
            departure_date_time like %s and A.city = %s and B.city = %s"""
            cursor.execute(query, ((depdate + "%"), departs, arrives))
    
            
    data1 = cursor.fetchall()  
    cursor.close()
    try:
        email = session['email']
    except:
        email = False
    if (email):
        print(session['email'])
        return render_template('client_results.html', data = data1, name = session['name'])
    else:
        return render_template('results.html', data = data1)

#Define route for login
@app.route('/client_login')
def Clogin():
	return render_template('client_login.html')

#Define route for register
@app.route('/client_register')
def Cregister():
	return render_template('client_register.html')

#Authenticates the login
@app.route('/CloginAuth', methods=['GET', 'POST'])
def CloginAuth():
    #grabs information from the forms
    email = request.form['email']
    password = str(hashlib.md5(request.form['password'].encode()).hexdigest())
    print(password)
    #cursor used to send queries
    cursor = conn.cursor()
	#executes query
    query = 'SELECT * FROM customer WHERE email = %s and password = %s'
    cursor.execute(query, (email, password))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if(data):
		#creates a session for the the user
		#session is a built in
        session['email'] = email
        return redirect(url_for('client_home'))
    else:
		#returns an error message to the html page
        error = 'Invalid login or username'
        return render_template('client_login.html', error=error)

#Authenticates the register
@app.route('/CregisterAuth', methods=['GET', 'POST'])
def CregisterAuth():
    #grabs information from the forms
    email = request.form['email']
    name = request.form['name']
    password = str(hashlib.md5(request.form['password'].encode()).hexdigest())
    dob = request.form['date_of_birth']
    state = request.form['state']
    city = request.form['city']
    street = request.form['street']
    building_no = request.form['building_no']
    phone_no = request.form['phone_no']
    passport_no = request.form['passport_no']
    passport_exp = request.form['passport_exp']
    passport_country = request.form['passport_country']
    
    
    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = 'SELECT * FROM customer WHERE email = %s'
    cursor.execute(query, (email))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    error = None
    if(data):
    	#If the previous query returns data, then user exists
    	error = "This user already exists"
    	return render_template('client_register.html', error = error)
    else:
    	ins = 'INSERT INTO customer VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    	cursor.execute(ins, (email, name, password, dob, state, city, street, building_no, phone_no, passport_no, passport_exp, passport_country))
    	conn.commit()
    	cursor.close()
    	return render_template('index.html')

@app.route('/client_home')
def client_home():
    
    email = session['email']
    cursor = conn.cursor()
    #executes query
    query = 'SELECT * FROM customer WHERE email = %s'
    cursor.execute(query, (email))
    data = cursor.fetchone()
    name = data['name']
    session['name'] = name
    cursor.close()
    return render_template('client_home.html', name = name)




@app.route('/view_flights', methods=['GET', 'POST'])
def view_flights():
    email = session['email']
    cursor = conn.cursor();
    query1 = """
            SELECT distinct ticketID, F.airline_name, F.flight_no, F.departure_date_time, F.departs_from, F.arrival_date_time, F.arrives_from, 
            sold_price, A.city as departure_city, B.city as arrival_city, rating
            FROM rates natural right outer join ticket as T, flight as F, airport as A, airport as B where
            departs_from = A.name and arrives_from = B.name and F.flight_no = T.flight_no and
            F.airline_name = T.airline_name and F.departure_date_time = T.departure_date_time
            and T.email = %s and F.departure_date_time < Now()
            """
    query2 = """SELECT distinct ticketID, flight.airline_name, flight.flight_no, flight.departure_date_time, flight.departs_from, flight.arrival_date_time, 
            flight.arrives_from, sold_price, A.city as departure_city, B.city as arrival_city
            FROM flight, ticket, airport as A, airport as B where
            departs_from = A.name and arrives_from = B.name and flight.flight_no = ticket.flight_no and
            flight.airline_name = ticket.airline_name and flight.departure_date_time = ticket.departure_date_time
            and email = %s and flight.departure_date_time > Now()"""

    cursor.execute(query1, (email))
    data = cursor.fetchall()
    cursor.execute(query2, (email))
    data2 = cursor.fetchall()
    name = session['name']
    cursor.close()
    print(data)
    return render_template('my_flights.html', data = data, data2 = data2, name = name)

@app.route('/my_spending', methods=['GET', 'POST'])
def render_spend():
    email = session['email']
    cursor = conn.cursor();
    query1 = "SELECT * FROM monthly_spend where email = %s and purchase_date_time > DATE_ADD(Now(), INTERVAL -6 Month)"
    query2 = "SELECT sum(spending) FROM monthly_spend where email = %s and purchase_date_time > DATE_ADD(Now(), INTERVAL -12 Month)"
    cursor.execute(query1, (email))
    data = cursor.fetchall()
    cursor.execute(query2, (email))
    total_data = cursor.fetchall()[0]['sum(spending)']
    processedY = []
    processedX = []
    for i in range(len(data)):
        processedX.append(data[i]['month'])
    for i in range(len(data)):
        processedY.append(int(data[i]['spending']))

    return render_template("my_spending.html", dataX = processedX, dataY = processedY, total = total_data)

@app.route('/date_range', methods=['GET', 'POST'])
def render_range():
    email = session['email']
    start = request.form['start']
    end = request.form['end']
    message = "Showing spending from %s to %s" % (start, end)
    cursor = conn.cursor();
    query1 = "SELECT * FROM monthly_spend where email = %s and purchase_date_time between %s and %s"
    query2 = "SELECT sum(spending) FROM monthly_spend where email = %s and purchase_date_time > DATE_ADD(Now(), INTERVAL -12 Month)"
    cursor.execute(query1, (email, start, end))
    data = cursor.fetchall()
    cursor.execute(query2, (email))
    total_data = cursor.fetchall()[0]['sum(spending)']
    processedY = []
    processedX = []
    for i in range(len(data)):
        processedX.append(data[i]['month'])
    for i in range(len(data)):
        processedY.append(int(data[i]['spending']))

    return render_template("my_spending.html", dataX = processedX, dataY = processedY, total = total_data, message = message)
    
    
@app.route('/rate', methods=['GET', 'POST'])
def rate():
    email = session['email']
    rating = request.form['rating']
    airline_name = request.form['airline_name']
    departure_date_time = request.form['departure_date_time']
    flight_no = request.form["flight_no"]
    comment = request.form['comment']
    cursor = conn.cursor();
    test_query = "select * from rates where email = %s and airline_name = %s and departure_date_time = %s and flight_no = %s"
    cursor.execute(test_query, (email, airline_name, departure_date_time, flight_no))
    data = cursor.fetchall()
    if data:
        query = """UPDATE rates
        SET rating = %s, comment = %s
        WHERE email = %s and airline_name = %s and departure_date_time = %s and flight_no = %s;"""
        cursor.execute(query, (rating, comment, email, airline_name, departure_date_time, flight_no))
    else:
        query = "INSERT INTO rates VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (email, airline_name, flight_no, departure_date_time, rating, comment))
    
    conn.commit()
    cursor.close()
    return redirect('/view_flights')

@app.route('/render_purchase', methods=['GET', 'POST'])
def render_purchase():
    cursor = conn.cursor();
    test_query = "select max(ticketID) from ticket"
    cursor.execute(test_query)
    data = cursor.fetchall()
    session['ticket_no'] = str(int(data[0]['max(ticketID)']) + 1)
    
    session['purchase_airline'] = request.form['airline_name']
    session['purchase_dep'] = request.form['departure_date_time']
    session['purchase_flight'] = request.form["flight_no"]
    session['sold_price'] = request.form["real_price"]
    airline_name = session['purchase_airline']
    flight_no = session['purchase_flight']
    departure_date_time = session['purchase_dep']
    
    test_query = """select percentage_full from flight_avail where 
    airline_name = %s and departure_date_time = %s and flight_no = %s"""
    
    cursor.execute(test_query, (airline_name, departure_date_time, flight_no))
    test_data = cursor.fetchall()
    cursor.close()
    if test_data[0]['percentage_full'] >= 100:
        cursor.close()
        return render_template("already_purchased.html")
    else:
        return render_template("purchase.html", airline = session['purchase_airline'], departure = session['purchase_dep'], flight = session['purchase_flight'], price = session['sold_price'])
    
@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
    ticketID = session['ticket_no']
    email = session['email']
    airline_name = session['purchase_airline']
    flight_no = session['purchase_flight']
    departure_date_time = session['purchase_dep']
    sold_price = session['sold_price']
    card_type = request.form['card_type']
    card_no = request.form['card_no']
    name_on_card = request.form['name_on_card']
    exp_date = request.form['exp_date'] + '-01'
    sec_code = request.form['sec_code']
    DT = datetime.datetime.now()
    purchase_date = DT.strftime("%Y-%m-%d %H:%M:%S")
    
    cursor = conn.cursor()
    '''
    test_query = "select percentage_full from flight_avail where airline_name = %s and departure_date_time = %s and flight_no = %s"
    cursor.execute(test_query, (airline_name, departure_date_time, flight_no))
    test_data = cursor.fetchall()
    
    if test_data[0]['percentage_full'] >= 100:
        cursor.close()
        return render_template("already_purchased.html")
    '''
    query = "INSERT INTO ticket VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (ticketID, email, airline_name, flight_no, departure_date_time, sold_price, purchase_date, card_type,
                   card_no, name_on_card, exp_date, sec_code))
    conn.commit()
    cursor.close()
    session.pop('ticket_no')
    session.pop('purchase_airline')
    session.pop('purchase_flight')
    session.pop('purchase_dep')
    session.pop('sold_price')

    
    return render_template("ticket.html", 
                    ticketID = ticketID, email = email, airline_name = airline_name,
                    flight_no = flight_no, departure_date_time = departure_date_time, sold_price = sold_price,
                    card_type = card_type, card_no = card_no, name_on_card = name_on_card, exp_date = exp_date,
                    purchase_date = purchase_date, name = session['name'])

@app.route('/logout')
def Clogout():
    '''
    session.pop('email')
    session.pop('name')
    '''
    session.clear()
    return redirect('/')



#Define route for login
@app.route('/staff_login')
def Slogin():
    cursor = conn.cursor()
    query = "select * from airline"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('staff_login.html', data = data)

#Define route for register
@app.route('/staff_register')
def Sregister():
    cursor = conn.cursor()
    query = "select * from airline"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('staff_register.html', data = data)

#Authenticates the login
@app.route('/SloginAuth', methods=['GET', 'POST'])
def SloginAuth():
    #grabs information from the forms
    username = request.form['username']
    password = str(hashlib.md5(request.form['password'].encode()).hexdigest())
    airline_name = request.form['airline_name']

    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    airline_name = request.form['airline_name']
    query = 'SELECT * FROM airline_staff WHERE username = %s and password = %s and airline_name = %s'
    cursor.execute(query, (username, password, airline_name))
    
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if(data):
        #creates a session for the the user
        #session is a built in
        session['username'] = username
        session['airline_name'] = airline_name
        return redirect(url_for('staff_home'))
    else:
        #returns an error message to the html page
        error = 'Invalid login or username'
        query = "select * from airline"
        cursor = conn.cursor()
        cursor.execute(query)
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('staff_login.html', data = data1, error=error)

#Authenticates the register
@app.route('/SregisterAuth', methods=['GET', 'POST'])
def SregisterAuth():
    #grabs information from the forms
    username = request.form['username']
    password = str(hashlib.md5(request.form['password'].encode()).hexdigest())
    airline_name = request.form['airline_name']
    dob = request.form['date_of_birth']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone_number = request.form['phone_number']
    
    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = 'SELECT * FROM airline_staff WHERE username = %s'
    cursor.execute(query, (username))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    error = None
    if(data):
        #If the previous query returns data, then user exists
        error = "This user already exists"
        query = "select * from airline"
        cursor.execute(query)
        data1 = cursor.fetchall()
        cursor.close()
        return render_template('staff_register.html', data = data1, error = error)
    else:
        ins = 'INSERT INTO airline_staff VALUES(%s, %s, %s, %s, %s, %s)'
        ins_phone = 'INSERT INTO phone_number VALUES(%s, %s)'
        cursor.execute(ins, (username, password, airline_name, first_name, last_name, dob))
        cursor.execute(ins_phone, (username, phone_number))
        conn.commit()
        cursor.close()
        return render_template('index.html')
@app.route('/staff_home')
def staff_home():
    
    username = session['username']
    airline_name = session['airline_name']
    cursor = conn.cursor()
    #executes query
    query1 = 'SELECT * FROM airline_staff WHERE username = %s'
    cursor.execute(query1, (username))
    data1 = cursor.fetchone()
    name = data1['first_name']
    session['first_name'] = name
    query2 = """SELECT * FROM flight WHERE airline_name = %s and departure_date_time BETWEEN Now() and DATE_ADD(NOW(), INTERVAL 30 DAY)"""
    cursor.execute(query2, (airline_name))
    data2 = cursor.fetchall()
    #airline_name = data2['airline_name']
    #session['airline_name'] = airline_name
    query3 = """SELECT DISTINCT planeID FROM airplane WHERE airline_name = %s"""
    cursor.execute(query3, (airline_name))
    data3 = cursor.fetchall()

    query4 = """SELECT DISTINCT departs_from FROM flight WHERE airline_name = %s"""
    cursor.execute(query4, (airline_name))
    data4 = cursor.fetchall()

    query5 = """SELECT DISTINCT arrives_from FROM flight WHERE airline_name = %s"""
    cursor.execute(query5, (airline_name))
    data5 = cursor.fetchall()

    query6 = """SELECT DISTINCT name FROM airport"""
    cursor.execute(query6)
    data6 = cursor.fetchall()

    cursor.close()
    return render_template('staff_home.html', data1 = data1, data2 = data2, data3 = data3, data4 = data4, data5 = data5, data6 = data6, username = username, airline_name = airline_name)

@app.route('/ViewFlights', methods=['GET', 'POST'])
def ViewFlights():
    username = session['username']
    airline_name = session['airline_name']
    departure_date_time_from = request.form['departure_date_time_from']
    departure_date_time_to = request.form['departure_date_time_to']
    departs_from = request.form['departs_from']
    arrives_from = request.form['arrives_from']
    cursor = conn.cursor();
    query = """SELECT flight_no, departure_date_time, departs_from, arrival_date_time, arrives_from, base_price, flight_status 
                FROM flight 
                WHERE airline_name = %s AND departure_date_time BETWEEN %s AND %s AND departs_from = %s AND arrives_from = %s"""
    cursor.execute(query, (airline_name, departure_date_time_from, departure_date_time_to, departs_from, arrives_from))
    data = cursor.fetchall()
    cursor.close()
    print(data)
    return render_template('ViewFlights.html', data = data, username = username, airline_name = airline_name)

@app.route('/ViewCustFlights', methods=['GET', 'POST'])
def ViewCustFlights():
    airline_name = session['airline_name']
    email = request.form['email']
    cursor = conn.cursor();
    query = """SELECT airline_name, flight_no, departure_date_time, email
                FROM ticket
                WHERE airline_name = %s and email = %s"""
    cursor.execute(query, (airline_name, email))
    data = cursor.fetchall()
    cursor.close()
    print(data)
    return render_template('ViewCustFlights.html', data = data, email = email, airline_name = airline_name)

@app.route('/ChangeFlightStatus', methods=['GET', 'POST'])
def ChangeFlightStatus():
    username = session['username']
    airline_name = session['airline_name']
    cursor = conn.cursor();
    query = "SELECT * FROM flight WHERE airline_name = %s" #and departure_date_time BETWEEN Now() and DATE_ADD(NOW(), INTERVAL 30 DAY)"
    cursor.execute(query, (airline_name))
    data = cursor.fetchall()
    query2 = "SELECT flight_status, COUNT(flight_status) as 'count' FROM flight WHERE airline_name = %s GROUP BY flight_status"#and departure_date_time BETWEEN Now() and DATE_ADD(NOW(), INTERVAL 30 DAY)"
    cursor.execute(query2, (airline_name))
    data2 = cursor.fetchall()
    cursor.close()
    print(data)
    return render_template('ChangeFlightStatus.html', data = data, data2 = data2, username = username, airline_name = airline_name)

@app.route('/flight_status', methods=['GET', 'POST'])
def flight_status():
    airline_name = session['airline_name']
    flight_status = request.form['flight_status']
    departure_date_time = request.form['departure_date_time']
    flight_no = request.form["flight_no"]
    cursor = conn.cursor();
    query = """UPDATE flight
    SET flight_status = %s
    WHERE airline_name = %s and flight_no = %s and departure_date_time = %s"""
    cursor.execute(query, (flight_status, airline_name, flight_no, departure_date_time))
    #data = cursor.fetchall()
    conn.commit()
    cursor.close()
    return redirect('/ChangeFlightStatus')

@app.route('/AddNewFlights', methods=['GET', 'POST'])
def AddNewFlights():
    #grabs information from the forms
    airline_name = session['airline_name']
    planeID = request.form['planeID']
    flight_no = request.form['flight_no']
    departure_date_time = request.form['departure_date_time']
    arrival_date_time = request.form['arrival_date_time']
    departs_from = request.form['departs_from']
    arrives_from = request.form['arrives_from']
    base_price = request.form['base_price']
    flight_status = request.form['flight_status']

    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = 'INSERT INTO flight (`planeID`, `airline_name`, `flight_no`, `departure_date_time`, `arrival_date_time`, `departs_from`, `arrives_from`, `base_price`, `flight_status`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    try:
        cursor.execute(query, (planeID, airline_name, flight_no, departure_date_time, arrival_date_time, departs_from, arrives_from, base_price, flight_status))
    except:
        error = 'Flight already exists or Invalid input'
        return render_template('staff_home.html', error = error)
    conn.commit()
    cursor.close()
    return redirect(url_for('staff_home'))

@app.route('/AddNewPlane', methods=['GET', 'POST'])
def AddNewPlane():
    airline_name = session['airline_name']
    planeID = request.form['planeID']
    seats = request.form['seats']
    cursor = conn.cursor()
    query = 'INSERT INTO `airplane` (`airline_name`, `planeID`, `seats`) VALUES (%s, %s, %s);'
    try:
        cursor.execute(query, (airline_name, planeID, seats))
    except:
        error = 'Plane already in the system or Invalid input'
        return render_template('staff_home.html', error = error)
    conn.commit()
    cursor.close()
    return redirect(url_for('staff_home'))

@app.route('/add_number', methods=['GET', 'POST'])
def AddPhoneNumber():
    username = session['username']
    number = request.form['phone_number']
    cursor = conn.cursor()
    query = 'INSERT INTO phone_number VALUES (%s, %s);'
    try:
        cursor.execute(query, (username, number))
    except:
        error = 'Plane already in the system or Invalid input'
        return render_template('staff_home.html', error = error)
    conn.commit()
    cursor.close()
    return redirect(url_for('staff_home'))

@app.route('/AddNewAirport', methods=['GET', 'POST'])
def AddNewAirport():
    name = request.form['name']
    city = request.form['city']
    cursor = conn.cursor()
    query = 'INSERT INTO `airport` (`name`, `city`) VALUES (%s, %s);'
    try:
        cursor.execute(query, (name, city))
    except:
        error = 'Airport already in the system or Invalid input'
        return render_template('staff_home.html', error = error)
    conn.commit()
    cursor.close()
    return redirect(url_for('staff_home'))

@app.route('/ViewFlightRatings', methods=['GET', 'POST'])
def ViewFlightRatings():
    username = session['username']
    airline_name = session['airline_name']
    cursor = conn.cursor();
    query1 = "SELECT email, airline_name, flight_no, departure_date_time, comment, rating FROM `rates` WHERE airline_name = %s"
    query2 = "SELECT airline_name, flight_no, departure_date_time, AVG(rating) AS 'rating' FROM `rates` WHERE airline_name = %s group by airline_name, flight_no, departure_date_time"
    cursor.execute(query1, (airline_name))
    data = cursor.fetchall()
    cursor.execute(query2, (airline_name))
    data2 = cursor.fetchall()
    cursor.close()
    print(data2)
    return render_template('ViewFlightRatings.html', data = data, data2 = data2, username = username, airline_name = airline_name)

@app.route('/CustomersInFlight', methods=['GET', 'POST'])
def CustomersInFlight():
    username = session['username']
    airline_name = session['airline_name']
    flight_no = request.form['flight_no']
    cursor = conn.cursor();
    query = """SELECT flight_no, departure_date_time, email 
                FROM ticket
                WHERE airline_name = %s and flight_no = %s"""
    cursor.execute(query, (airline_name, flight_no))
    data = cursor.fetchall()
    cursor.close()
    print(data)
    return render_template('CustomersInFlight.html', data = data, username = username, airline_name = airline_name)

@app.route('/ViewFrequentCustomers', methods=['GET', 'POST'])
def ViewFrequentCustomers():
    username = session['username']
    airline_name = session['airline_name']
    cursor = conn.cursor();
    query1 = """SELECT email, name, date_of_birth, state, city, street, building_no, phone_no
                FROM customer NATURAL JOIN ticket NATURAL JOIN flight 
                WHERE airline_name = %s AND email = (SELECT MAX(email) FROM customer) AND purchase_date_time BETWEEN DATE_SUB(NOW(), INTERVAL 365 DAY) and NOW() group by email"""
    cursor.execute(query1, (airline_name))
    data1 = cursor.fetchall()
    query2 = """SELECT email, name, date_of_birth, state, city, street, building_no, phone_no, ticketID, flight_no, departure_date_time, departs_from, arrives_from, purchase_date_time, base_price, sold_price, flight_status 
                FROM customer NATURAL JOIN ticket NATURAL JOIN flight 
                WHERE airline_name = %s 
                ORDER BY email"""
    cursor.execute(query2, (airline_name))
    data2 = cursor.fetchall()
    cursor.close()
    print(data1)
    print(data2)
    return render_template('ViewFrequentCustomers.html', data1 = data1, data2 = data2, username = username, airline_name = airline_name)

@app.route('/ViewQuarterlyRevenueEarned', methods=['GET', 'POST'])
def ViewQuarterlyRevenueEarned():
    username = session['username']
    airline_name = session['airline_name']
    cursor = conn.cursor();
    query1 = """SELECT COALESCE(SUM(sold_price), 0) as 'Revenue' 
                FROM `ticket` 
                WHERE airline_name = %s AND purchase_date_time BETWEEN DATE_SUB(NOW(), INTERVAL 365 DAY) AND (DATE_SUB(NOW(), INTERVAL 275 DAY))"""
    cursor.execute(query1, (airline_name))
    data1 = cursor.fetchall()
    query2 = """SELECT COALESCE(SUM(sold_price), 0) as 'Revenue' 
                FROM `ticket` 
                WHERE airline_name = %s AND purchase_date_time BETWEEN DATE_SUB(NOW(), INTERVAL 275 DAY) AND (DATE_SUB(NOW(), INTERVAL 184 DAY))"""
    cursor.execute(query2, (airline_name))
    data2 = cursor.fetchall()
    query3 = """SELECT COALESCE(SUM(sold_price), 0) as 'Revenue' 
                FROM `ticket` 
                WHERE airline_name = %s AND purchase_date_time BETWEEN DATE_SUB(NOW(), INTERVAL 184 DAY) AND (DATE_SUB(NOW(), INTERVAL 92 DAY))"""
    cursor.execute(query3, (airline_name))
    data3 = cursor.fetchall()
    query4 = """SELECT COALESCE(SUM(sold_price), 0) as 'Revenue' 
                FROM `ticket` 
                WHERE airline_name = %s AND purchase_date_time BETWEEN DATE_SUB(NOW(), INTERVAL 92 DAY) AND NOW()"""
    cursor.execute(query4, (airline_name))
    data4 = cursor.fetchall()
    cursor.close()
    print(data1)
    print(data2)
    print(data3)
    print(data4)
    return render_template('ViewQuarterlyRevenueEarned.html', data1 = data1[0]['Revenue'], data2 = data2[0]['Revenue'], data3 = data3[0]['Revenue'], data4 = data4[0]['Revenue'], username = username, airline_name = airline_name)

@app.route('/ViewTopDestinations', methods=['GET', 'POST'])
def ViewTopDestinations():
    username = session['username']
    airline_name = session['airline_name']
    cursor = conn.cursor();
    #CREATE VIEW topdest_last_three_months AS SELECT arrives_from, city, COUNT(arrives_from) AS 'count' FROM flight, airport WHERE arrives_from = name AND departure_date_time BETWEEN DATE_SUB(NOW(), INTERVAL 90 DAY) AND NOW()GROUP BY arrives_from
    #CREATE VIEW topdest_last_year AS SELECT arrives_from, city, COUNT(arrives_from) AS 'count' FROM flight, airport WHERE arrives_from = name AND departure_date_time BETWEEN DATE_SUB(NOW(), INTERVAL 365 DAY) AND NOW()GROUP BY arrives_from
    query1 = """SELECT city, count
                FROM `topdest_last_three_months` 
                order by count desc
                limit 3;"""
    cursor.execute(query1)
    data1 = cursor.fetchall()
    query2 = """SELECT city, count 
                FROM `topdest_last_year` 
                order by count desc
                limit 3;"""
    cursor.execute(query2)
    data2 = cursor.fetchall()
    cursor.close()
    print(data1)
    print(data2)
    return render_template('ViewTopDestinations.html', data1 = data1, data2 = data2, username = username, airline_name = airline_name)

@app.route('/ViewReports', methods=['GET', 'POST'])
def ViewReports():
    username = session['username']
    airline_name = session['airline_name']
    fromtime = request.form['from_departure_date_time']
    totime = request.form['to_departure_date_time']
    cursor = conn.cursor();
    query1 = "SELECT airline_name, COUNT(ticketID) as No_ticket_sold FROM ticket WHERE purchase_date_time  > %s AND purchase_date_time < %s GROUP BY airline_name"
    cursor.execute(query1, (fromtime, totime))
    data1 = cursor.fetchall()
    query2 = "SELECT airline_name, COUNT(ticketID) as No_ticket_sold FROM ticket WHERE purchase_date_time  BETWEEN DATE_SUB(NOW(), INTERVAL 365 DAY) AND NOW() GROUP BY airline_name"
    cursor.execute(query2)
    data2 = cursor.fetchall()
    query3 = "SELECT airline_name, COUNT(ticketID) as No_ticket_sold FROM ticket WHERE purchase_date_time  BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW() GROUP BY airline_name"
    cursor.execute(query3)
    data3 = cursor.fetchall()
    query4 = """SELECT month, revenue FROM monthly_revenue WHERE airline_name = %s ORDER BY month"""
    cursor.execute(query4, (airline_name))
    data4 = cursor.fetchall()
    processedY = []
    processedX = []
    for i in range(len(data4)):
        processedX.append(data4[i]['month'])
    for i in range(len(data4)):
        processedY.append(int(data4[i]['revenue']))
    cursor.close()
    print(data1)
    print(data2)
    print(data3)

    return render_template("ViewReports.html", data1 = data1, data2 = data2, data3 = data3, dataX = processedX, dataY = processedY, username = username)

@app.route('/Slogout')
def Slogout():
    '''
    session.pop('username')
    session.pop('airline_name')
    '''
    session.clear()
    return redirect('/')


app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION

app.secret_key = 'hello'
if __name__ == "__main__":
	app.run('127.0.0.1', 5200, debug = True)
