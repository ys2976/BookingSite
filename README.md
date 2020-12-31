# Shanghai New York University Project for Databases CSCI-SHU 213 Summer 2019
### Professor: Ratan Dey
### Team member: Neal Shu, Roberto Noel

## Objective
The objective of this course project is to provide a realistic experience in the design process of a
relational database and corresponding applications. We will focus on conceptual design, logical design,
implementation, operation, maintenance of a relational database. We will also implement an associated
web based application to communicate with the database (retrieve information, store information etc). 

## Project Overview
The course project for this semester is online Air Ticket Reservation System. Using this system,
customers can search for flights (one way or round trip), purchase flights ticket, view their future flight
status or see their past flights etc. There will be two types of users of this system - Customers and Airline
Staff (Administrator). Airline Staff will add new airplanes, create new flights, and update flight status. In
general, this will be simple air ticket reservation system. 

## Project Description
There are several airports (**Airport**), each consisting of a unique name and a city.<br /><br />
There are several airlines (Airline), each with a unique name. Each airline owns several airplanes. An
airplane (**Airplane**) consists of the airline that owns it, a unique identification number within that airline,
and the amount of seats on the airplane.<br /><br />
Each airline operates flights (**Flight**), which consist of the airline operating the flight, a flight number,
departure airport, departure date and time, arrival airport, arrival date and time, a base price, and the
identification number of the airplane for the flight. Each flight is identifiable using flight number and
departure date and time together within that airline.<br /><br />
A ticket (**Ticket**) can be purchased for a flight by a Customer and will consist of the customer’s email
address, the airline name, the flight number, sold_price (may be different from base price of the flight),
payment information (card type - credit/debit, card number, name on card, expiration date), purchase
date and time. Each ticket will have a ticket ID number which is unique in this System.
Anyone (including users not signed in) can see flights (future flights) based on the source airport,
destination airport, source city, or destination city, departure date for one way (departure and return
dates for round trip). Additionally, anyone can see the status (delayed/on time etc.) of the flight based
on an airline and flight number combination and arrival or departure date.<br /><br />
There are two types of users for this system: Customer and Airline Staff.<br /><br />
### **Customer:**<br /><br />
Each Customer has a name, email, password, address (composite attribute consisting of
building_number, street, city, state), phone_number, passport_number, passport_expiration,
passport_country, and date_of_birth. Each Customer’s email is unique, and they will sign into the
system using their email address and password.<br /><br />
Customers must be logged in to purchase a flight ticket.<br /><br />
Customers can purchase a ticket for a flight as long as there is still room on the plane. This is based on
the amount of tickets already booked for the flight and the seating capacity of the airplane assigned to
the flight and customer needs to pay the associated price for that flight. Ticket price of a flight will be
determined based on two factors – minimum/base price as set by the airline and additional price which
will depend on demand of that flight. If 70% of the capacities is already booked/reserved for that flight,
extra 20% will be added with the minimum/base price. Customer can buy tickets using either credit card
or debit card. We want to store card information (number and expiration date and name on the card but
not the security code) along with purchased date, time.<br /><br />
Customer will be able to see their future flights or previous flights taken for the airline they logged in.<br /><br />
Customer will be able to rate and comment on their previous flights taken for the airline they logged in.<br /><br />
### **Airline Staff:**<br /><br />
Each Airline Staff has a unique username, a password, a first name, a last name, a date of birth, may
have more than one phone number, and the airline name that they work for. One Airline Staff works for
one particular airline.<br /><br />
Airline Staff will be able to add new airplanes into the system for the airline they work for.<br /><br />
Airline Staff will set flight statuses in the system.<br /><br />
Each Airline Staff can create new flights only for the particular airline that they work for by inserting all
necessary information and will set the ticket base price for flight. They will also be able to see all ontime, future, and previous flights for the airline that they work for, as well as a list of passengers for the
flights.<br /><br />
In addition, Airline Staff will be able to see a list of all flights a particular Customer has taken only on that
particular airline.<br /><br />
Airline Staff will be able to see each flight’s average ratings and all the comments and ratings of that
flight given by the customers.<br /><br />
Airline Staff will also be able to see the most frequent customer within the last year, see the amount of
tickets sold each month, see the total amount of revenue earned etc.<br /><br />
Airline Staff can query for how many flights get delayed/on-time etc.<br /><br />

## Use Cases
**REQUIRED Application Use Cases (aka features):**<br /><br />
1. **View Public Info:** All users, whether logged in or not, can<br /><br />
a. Search for future flights based on source city/airport name, destination city/airport name,
departure date for one way (departure and return dates for round trip).<br /><br />
b. Will be able to see the flights status based on airline name, flight number, arrival/departure
date.<br /><br />
2. **Register:** 2 types of user registrations (Customer and Airline Staff) option via forms.<br /><br />
3. **Login:** 2 types of user login (Customer and Airline Staff). Users enters their username (email address
will be used as username), x, and password, y, via forms on login page. This data is sent as POST
parameters to the login-authentication component, which checks whether there is a tuple in the Person
table with username=x and the password = md5(y).<br /><br />
a. If so, login is successful. A session is initiated with the member’s username stored as a session
variable. Optionally, you can store other session variables. Control is redirected to a component that
displays the user’s home page.<br /><br />
b. If not, login is unsuccessful. A message is displayed indicating this to the user.<br /><br />
Note: In real applications, members’ passwords are stored as md5/other hashes, not as plain text. This
keeps the passwords more secure, in case someone is able to break into the system and see the
passwords. You can perform the hash using MySQL’s md5 function or a library provided with your host
language.) Once a user has logged in, reservation system should display his/her home page. Also, after
other actions or sequences of related actions, are executed, control will return to component that
displays the home page. The home page should display<br /><br />
c. Error message if the previous action was not successful,<br /><br />
d. Some mechanism for the user to choose the use case he/she wants to execute. You may
choose to provide links to other URLS that will present the interfaces for other use cases, or you
may include those interfaces directly on the home page.<br /><br />
e. Any other information you’d like to include. For example, you might want to show customer's
future flights information on the customer's home page, or you may prefer to just show them
when he/she does some of the following use cases.<br /><br />
### **Customer use cases:**<br /><br />
After logging in successfully a user(customer) may do any of the following use cases:<br /><br />
4. **View My flights:** Provide various ways for the user to see flights information which he/she purchased.
The default should be showing for the future flights. Optionally you may include a way for the user to
specify a range of dates, specify destination and/or source airport name or city name etc.<br /><br />
5. **Search for flights:** Search for future flights (one way or round trip) based on source city/airport name,
destination city/airport name, dates (departure or return).<br /><br />
6. **Purchase tickets:** Customer chooses a flight and purchase ticket for this flight, providing all the
needed data, via forms. You may find it easier to implement this along with a use case to search for
flights.<br /><br />
6. **Give Ratings and Comment on previous flights:** Customer will be able to rate and comment on their
previous flights (for which he/she purchased tickets and already took that flight) for the airline they
logged in.<br /><br />
7.**Track My Spending:** Default view will be total amount of money spent in the past year and a bar
chart showing month wise money spent for last 6 months. He/she will also have option to specify a
range of dates to view total amount of money spent within that range and a bar chart showing month
wise money spent within that range.<br /><br />
8.**Logout:** The session is destroyed and a “goodbye” page or the login page is displayed.<br /><br />
### **Airline Staff use cases:**<br /><br />
After logging in successfully an airline staff may do any of the following use cases:<br /><br />
4. **View flights:** Defaults will be showing all the future flights operated by the airline he/she works for
the next 30 days. He/she will be able to see all the current/future/past flights operated by the airline
he/she works for based range of dates, source/destination airports/city etc. He/she will be able to see
all the customers of a particular flight.<br /><br />
5. **Create new flights:** He or she creates a new flight, providing all the needed data, via forms. The
application should prevent unauthorized users from doing this action. Defaults will be showing all the
future flights operated by the airline he/she works for the next 30 days.<br /><br />
6. **Change Status of flights:** He or she changes a flight status (from on-time to delayed or vice versa) via
forms.<br /><br />
7. **Add airplane in the system:** He or she adds a new airplane, providing all the needed data, via forms.
The application should prevent unauthorized users from doing this action. In the confirmation page,
she/he will be able to see all the airplanes owned by the airline he/she works for.<br /><br />
8. **Add new airport in the system:** He or she adds a new airport, providing all the needed data, via
forms. The application should prevent unauthorized users from doing this action.<br /><br />
9. **View flight ratings:** Airline Staff will be able to see each flight’s average ratings and all the comments
and ratings of that flight given by the customers.<br /><br />
10. **View frequent customers:** Airline Staff will also be able to see the most frequent customer within
the last year. In addition, Airline Staff will be able to see a list of all flights a particular Customer has
taken only on that particular airline.<br /><br />
11. **View reports:** Total amounts of ticket sold based on range of dates/last year/last month etc. Month
wise tickets sold in a bar chart.<br /><br />
12. **View quarterly revenue earned:** Draw a pie chart for showing total amount of revenue earned from
for each quarter of the last year.<br /><br />
13. **View Top destinations:** Find the top 3 most popular destinations for last 3 months and last year.<br /><br />
14. **Logout:** The session is destroyed and a “goodbye” page or the login page is displayed.<br /><br />

## File Description
Quick Note: Make sure path and static path is correct for python file.

1. pject.py ~ python backend, uses flask and pymysql to render templates and execute queries. (must change static folder path etc.)

2. background.jpg ~ background image for landing page and client home

3. server_setup.sql ~ sets up mysql server with tables and inserts

4. ratan_inserts.sql ~ a list of Professor(Ratan Dey)’s use case inserts (already included in setup)

5. bootstrap.min.css ~ css for landing page

6. style.css ~ css for landing page

7. Inserts.sql ~ alternative inserts (not included in setup)

8. index.html ~ landing page with public flight search 

9. results.html ~ flight search result page w/o purchase option

10. client_register.html ~ client registration page

11. client_login.html ~ client login page

12. client_home.html ~ client home page with public flight search

13. client_results.html ~ flight search result page with purchase option

14. purchase.html ~ purchase form to get payment info

15. already_purchased.html ~ page warning that flight is full and cannot be purchased

16. ticket.html ~ displays purchase and ticket information after purchase is made

17. my_flights.html ~ displays previous and upcoming flight information and allows rating for past flights

18. my_spending.html ~ shows clients annual spending along with a bar chart displaying spending for past 6 months and an option to view spending in a range

19. staff_home.html script to generate staff home page

20. staff_login.html to generate staff login page

21. staff_register.html to generate staff register page

22. ViewCustFlight.html to generate a page to see flights taken by a specific customer

23. ViewFlightRatings.html to generate a page to see ratings of flights of a specific airline, plus the average ratings

24. ViewFlights.html to generate a page to see flights of a specific airline based on range of dates and destinations etc.

25. ViewFrequentCustomer.html to generate a page to see the most frequent customer of a specific airline in the last year, plus all the flights taken by customers of that airline

26. ViewQuarterlyRevenueEarned.html to generate a page with a pie chart showing quarterly revenue earned

27. ViewReports.html to generate a page showing the number of tickets sold per airline based on a time range

28. ViewTopDestinations.html to generate a page showing top three destinations for the last three months and last year.

29. ChangeFlightStatus.html to generate a page showing all flights of a specific airline, where flight status can be edited by staff

30. CustomersInFlight.html to generate a page showing all customers on a specific flight
