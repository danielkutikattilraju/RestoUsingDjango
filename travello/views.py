from django.shortcuts import render
from .models import Menu

# Create your views here.

def index(request): 

    menu1 = Menu()
    menu1.name = 'Egg Rice'
    menu1.price = 50
    menu1.offer = False
    menu1.des = 'Boiled rice with egg and some delicious veggies'
    menu1.img = 'menu-item-1.png'

    menu2 = Menu()
    menu2.name = 'Paneer Biriyani'
    menu2.price = 180
    menu2.offer = True
    menu2.des = 'Boiled rice with Paneer and some delicious veggies'
    menu2.img = 'menu-item-2.png'

    menu3 = Menu()
    menu3.name = 'Veg Meals'
    menu3.price = 90
    menu3.offer = True
    menu3.des = 'Boiled rice with curries'
    menu3.img = 'menu-item-3.png'

    # menus = [menu1, menu2, menu3]

    menus = Menu.objects.all()
    return render(request, 'index.html', {'menus': menus})