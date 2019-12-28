from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import models
import json
from random import randint
# Create your views here.
""" def index(request):
    return HttpResponse("Project 3: TODO") """

def ColorRandom():
    a = "0123456789ABCDEF"
    c = "#"
    for i in range(6):
        c+=a[(randint(0,250)*randint(0,250)+randint(0,500))%16]
    return c


def menu(request):
    if (request.user.get_username()):
        context = {
            "regular_pizza": zip(models.Pizza.objects.filter(tipe="RP", size="S"), models.Pizza.objects.filter(tipe="RP", size="L")),
            "sicilian_pizza": zip(models.Pizza.objects.filter(tipe="SP", size="S"), models.Pizza.objects.filter(tipe="SP", size="L")),
            "toppings": models.Topping.objects.all(),
            "subs": zip(models.Pizza.objects.filter(tipe="Sub", size="S"), models.Pizza.objects.filter(tipe="Sub", size="L")),
            "pasta": models.Pizza.objects.filter(tipe="Pasta"),
            "salad": models.Pizza.objects.filter(tipe="Salad"),
            "dinnerplatters": zip(models.Pizza.objects.filter(tipe="DP", size="S"), models.Pizza.objects.filter(tipe="DP", size="L"))
        }

        return render(request, "orders/menu.html", context)
    else:
        return redirect("/login/")


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        print(username)
        password = request.POST["password"]
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "orders/login.html", {"message": "Login"})


def topink(request):
    context = {

        "limit": 3,
        "toppings": models.Topping.objects.all()
    }
    return render(request, "orders/topping.html", context)


def registration(request):
    context = {
        "client": models.Client.objects.all(),
        "client2": User.objects.all()
    }
    if request.method == 'POST':
        user = User.objects.create_user(request.POST.get(
            'username'), request.POST.get('email'), request.POST.get('password'))
        user.first_name = request.POST.get('name')
        user.last_name = request.POST.get('lastname')
        user.save()
        print("------------------------")
        print(user.first_name)
        print(user.last_name)
        print("------------------------")

        post = models.Client()
        post.firstname = request.POST.get('name')
        post.lastname = request.POST.get('lastname')
        post.username = request.POST.get('username')
        post.password = request.POST.get('password')
        post.email = request.POST.get("email")
        post.save()

        return render(request, "orders/register.html", context)

    else:
        return render(request, "orders/register.html", context)


def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "orders/menu.html", context)


def logout_view(request):
    logout(request)
    # return render(request, "orders/login.html", {"message": "Logged out."})
    return redirect("/login/")


def cart(request):

    Carrito = models.Carrito.objects.filter(userID=request.user.get_username())
    suma = 0
    productos = []
    indice = []
    for i, car in enumerate(Carrito):
        # print(vars(car))
        p = models.Pizza.objects.get(id=car.productID)
        productos.append(p)
        indice.append(i+1)
        suma += p.price

    # print(models.Carrito.objects.all())
    return render(
        request,
        "orders/cart.html",
        {"Cart": zip(indice, productos, Carrito),
         "Cart2": Carrito,
         "precio": round(suma, 2)
         }
    )


def cancel(request):
    models.Carrito.objects.all().delete()
    return redirect("/menu/")


def accept(request):
    cart = models.Carrito.objects.filter(userID=request.user.get_username())
    for i in cart:
        o = models.Order(productID=i.productID,
                         topings=i.topings, userID=i.userID)
        o.save()
    models.Carrito.objects.filter(userID=request.user.get_username()).delete()
    return render(request, "orders/confirmedOrder.html")


def AddtoCart(request):
    print("entre add to cart")
    try:
        lista = request.POST["lista"]
        Pid = request.POST["productID"]
        print(lista)
        topping = lista
        print(topping)
        c = models.Carrito(
            productID=Pid, userID=request.user.get_username(), topings=topping)
        c.save()
    except:
        pass

    Carrito = models.Carrito.objects.filter(userID=request.user.get_username())

    suma = 0
    productos = []
    indice = []
    for i, car in enumerate(Carrito):
        # print(vars(car))
        p = models.Pizza.objects.get(id=car.productID)
        productos.append(p)
        indice.append(i+1)
        suma += p.price

    # print(models.Carrito.objects.all())
    return render(
        request,
        "orders/cart.html",
        {"Cart": zip(indice, productos, Carrito),
         "Cart2": Carrito,
         "precio": round(suma, 2)
         }
    )


def selectTopping(request, product):

    product = models.Pizza.objects.get(id=product)
    print(product.product[0])
    print(request.method, "////////////////////**********")
    if product.product[0] in "123":
        context = {
            "product": product,
            "toppings": models.Topping.objects.all(),
            "limit": int(product.product[0])
        }
        print(context)
        print(product.product, "-------------------1")
        return render(request, "orders/topping.html", context)
    else:
        print(product.product, "-------------------2")
        c = models.Carrito(productID=product.id,
                           userID=request.user.get_username(), topings="")
        c.save()
        Carrito = models.Carrito.objects.filter(
            userID=request.user.get_username())

        suma = 0
        productos = []
        indice = []
        for i, car in enumerate(Carrito):
            # print(vars(car))
            p = models.Pizza.objects.get(id=car.productID)
            productos.append(p)
            indice.append(i+1)
            suma += p.price

        return render(
            request,
            "orders/cart.html",
            {
                "Cart": zip(indice, productos, Carrito),
                "Cart2": Carrito,
                "precio": round(suma, 2)
            }
        )


def viewOrders(request):
    orders = models.Order.objects.all()
    productos = []
    indice = []
    for i, order in enumerate(orders):
        p = models.Pizza.objects.get(id=order.productID)
        productos.append(p)
        indice.append(i+1)
    context = {
        "Orders": zip(indice, productos, orders),
        "Orders2": bool(orders)
    }
    if request.user.is_staff:
        return render(request, "orders/orders.html", context)
    else:
        return menu(request)


def AddComment(request):

    if request.method == 'POST':

        username = request.user.get_username()
        comment = request.POST["comment"]
        rank = request.POST["rank"]
        c = models.Comment(
            userID=username,
            comment=comment,
            rank=rank
        )
        c.save()

    comments = models.Comment.objects.all()
    colors = []
    for i in comments:
        colors.append(ColorRandom())
    context = {
        "Comments": zip(colors,comments)
    }
    
    return render(request, "orders/comment.html", context)
