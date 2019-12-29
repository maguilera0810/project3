import csv
from django.db import models

class Pizza(models.Model):

    id = models.IntegerField(
        primary_key=True
    )
    product = models.CharField(
        max_length=64,
        null=False
    )
    tipe = models.CharField(
        max_length=64,
        null=False
    )
    size = models.CharField(
        max_length=64,
        null=False
    )
    price = models.FloatField(
        null=False
    )


class Topping(models.Model):
    product = models.CharField(
        max_length=64,
        null=False,
        default="")
    tipo = models.CharField(
        max_length=64
    )


class Client(models.Model):
    username = models.CharField(
        max_length=64,
        unique=True,
        primary_key=True
    )
    password = models.CharField(
        max_length=64
    )
    firstname = models.CharField(
        max_length=64
    )
    lastname = models.CharField(
        max_length=64,
        unique=True
    )
    email = models.EmailField()
    logeado = models.BooleanField(
        default=False
    )


class Order(models.Model):
    userID = models.CharField(
        max_length=64
    )
    productID = models.CharField(
        max_length=64
    )
    topings = models.CharField(
        max_length=64
    )


class Carrito(models.Model):
    userID = models.CharField(max_length=64, null=False)
    productID = models.CharField(max_length=64)
    topings = models.CharField(max_length=64)


class Comment(models.Model):
    userID = models.CharField(
        max_length=64,
        null=False
    )
    comment = models.CharField(
        max_length=300,
        null=True
    )
    rank = models.IntegerField(
        max_length=64,
        null=False
    )
<<<<<<< HEAD
=======


#from orders.models import Pizza
#from orders.models import Topping
>>>>>>> 86caa135e477a80d3f7e6ae1f2777ad8045f6188
