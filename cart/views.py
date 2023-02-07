from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

from auction.models import Products, Auction
import datetime

# Create your views here.
# Product, Price, Winner

def cartPage(request):
    context = {}
    if request.user.is_authenticated:
        user_name = request.user
        auction = Auction.objects.filter(user = user_name).values()
        prods = []
        cart = []
        for prod in auction:
            if prod['product_id'] not in prods:
                prods.append(prod['product_id'])
        for prod in prods:
            product = Products.objects.get(id = prod)
            cur_time = datetime.datetime.now()
            if cur_time > product.end_time:
                price = product.current_val
                auction = Auction.objects.filter(product = product).filter(last_bid_val = price).values()
                if auction[0]['user_id'] == request.user.id:
                    cart.append(product)
        context = {
            'cart': cart,
        }
    return render(request, 'cart/cart.html', context)