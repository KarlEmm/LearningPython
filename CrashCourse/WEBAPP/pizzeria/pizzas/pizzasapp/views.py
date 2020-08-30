from django.shortcuts import render
from .models import Pizza

def index(request):
  return render(request, 'pizzasapp/index.html')

def pizzas(request):
  pizzas = Pizza.objects.all()
  context = {'pizzas': pizzas}
  return render(request, 'pizzasapp/pizzas.html', context)

def pizza(request, pizza_id):
  pizza = Pizza.objects.get(id=pizza_id)
  toppings = pizza.toppings_set.all()
  context = {'pizza': pizza, 'toppings': toppings}
  return render(request, 'pizzasapp/pizza.html', context)