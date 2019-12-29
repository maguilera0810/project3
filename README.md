# Project 3

Web Programming with Python and JavaScript

Welcome to Project 3: Pizza

Youtube:
    https://youtu.be/b97jxoBaobo

Structure: 

Orders directory:
    -Migrations folder: It Contains all of the migrations. These migrations were done to create the database and its tables with their respective variable on each one of then.
    
    -Static fonder: Contains images, css and javascript files.
    
    -Templates folder: Contains all of the html files:

        - carrito.html: It shows all of the orders which have been made by the current user.

        - comment.html: It shows all of the the comments fromm all the users, and the user is able to add a new comment.

        - confirmedOrder.html: It appears at the moment when the user has completed its order.

        - layout.html: Contains all the links to css and boostrap which is extended to others html file.

        - login.html: The login page.

        - menu.html: Here appears all the items form the menu. On this page the user can select a product.

        - orders.html: This page is only showed to the users which have the corresponding permission (in this case staff users).

        - register.html: This page allows a new user to register.

        - topping.html: This page shows all the toppings, and the users are able to select topings.

- admin.py: THis file contains all of the tables created on models.py and the super user will be able to manipulated them.

- models.py: This file contanains all the tables for the database were created (Pizza, Topping, Client, Order, Carrito, Comment)

- urls.py: On this file is defined the paths.

- views.py: This file contains the logic of the server.

- prod_pizza.txt and prod_top.txt: Those files contain the data to fill up Pizza and Topping tables.

- import.py: The content on this file is used to insert automatically all of the elemens from prod_pizza.txt and prod_top.txt into the tables.
    You have to write on terminal "python3 manage shell". Then copy the content of the import.py file

Personal touch: As a aditional feature i implement the option of make comments about the page, this implementation can be found on views.py. 
