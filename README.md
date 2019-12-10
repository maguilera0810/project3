# Project 3

Web Programming with Python and JavaScript

Welcome to Project 3: Pizza

The structure of the following project goes as follows: 

Inside orders directory we can find 3 folders:
    -migrations folder which contains all of the migrations. These migrations were done to create the database and its tables with their respective variable on each one of theh.
    -static fonder contains both css and js files.
    -templates folder contains all of the html files used in this project:
        > base.html: contains a navBar which is extended to almost every other html file.  It shows options like login, logout, register, etc.
        > carrito.html: shows all of the orders which have been made by an specific user.
        > confirmedOrder.html: it appears at the moment when the user has completed its order.
        > login.html: Corresponds to the login page.
        > menu.html: Here appears all of the menu from Pinoccio's Pizza place. On this page the user logged is able to select the
        product which he/she wants to buy.
        >orders.html: this page is only showed to the users which have the corresponding permission (boolean value given on the users table). All of the orders which have been placed by every user can be seen here.
        >register.html: This page allows a new user to register, by giving its username, name, lastname, password, and email.
        >topping.html: As it was seen on Pinoccio's page, a user is able to choose a pizza with 1,2 or 3 toppings. Those topings can
        be selected on this page.
    
    In addition to the folders previously mentioned, there are also a couple of python files:
        > admin.py: is used to register all of the tables created on models.py
        > models.py: on this file, all of the tables for the database were created (Pizza, Topping, Client, Order, Carrito)
        > urls.py: is used to define all of the corresponding paths with their corresponding links, functions calls, and names.
        > views.py: it contains the logic of the server, on this file, all of the functions  have been defined. For example, functions for login, logout, add a new product to cart, adding orders, etc.

Now, pizza directory contains  some predetermined fles given by django itself.

data.txt & data1.txt files contain the data to fill up Pizza and Topping tables.
import.py file is used to insert automatically all of the elemens from data.txt and data1.txt into the tables.

Personal touch made on this project was to send an email of confirmation to the user which has placed a new order. the funtions used to achieve this corresponds to accept(request) and send_mail(text,email), these functions can be found on views.py. 

Note: givent the fact that the email being sent is through mailgun api, result can be seen on OrderReceived.png. Also, you must create first a superuser in order to being able to access to "See my Orders" page.