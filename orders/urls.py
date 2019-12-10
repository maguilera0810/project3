from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.menu,name = "index"),
    path("menu/", views.menu, name="menu"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("confirm", views.AddtoCart, name="Cart"),
    path("<int:product>", views.selectTopping, name="topping"),
    path("carrito/", views.cart, name="ShowCarrito"),
    path("confirmedOrder/", views.accept, name="Confirmado"),
    path("orders/", views.viewOrders, name="Ordenes"),
    path("cancel/", views.cancel, name="Cancel"),
    path("comments/", views.AddComment, name="Comment")
   
    #path("toppings/")views.logout_view, name="toppings")
]
