import csv
from orders.models import Pizza
from orders.models import Topping

f = open('prod_pizza.txt', 'r')
for line in f:
    line = line.rstrip('\n').split(',')
    print(line)
    product = Pizza()
    product.product = line[0]
    product.tipe = line[1]
    product.size = line[2]
    product.price = float(line[3]) 
    product.save()

f.close()


f = open('prod_top.txt', 'r')
for line in f:
    line = line.rstrip('\n').split(',')
    print(line)
    product = Topping()
    product.product = line[0]
    product.tipo = line[1]
    product.save()

f.close()
