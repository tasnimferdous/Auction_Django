from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Products, Auction
import datetime
# Create your views here.

def home(request):
    products = Products.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'auction/index.html', context)

def auction(request,prod_id):
    product = Products.objects.get(id = prod_id)
    context = {
        'product': product,
    }
    msg = ""
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            bid_value = int(request.POST.get('place_bid'))
            bid_time = datetime.datetime.now()
            if user.last_name == "Buyer":
                if bid_time > product.start_time and bid_time < product.end_time:
                    if bid_value > int(product.current_val):
                        product.current_val = bid_value
                        last_bid_val = bid_value
                        product.save(update_fields=['current_val'])
                        msg = "Bid placed successfully!"
                        context = {
                            'product': product,
                            'msg': msg,
                        }
                        bid = Auction(product = product, user = user, last_bid_val = bid_value, last_bid_time = bid_time)
                        bid.save()
                    else:
                        msg = "Please, place a higher bid!"
                        context = {
                            'product': product,
                            'msg': msg,
                        }
                else:
                    msg = "Sorry! Time Limit Exceeded Or Yet To Start!"
                    context = {
                        'product': product,
                        'msg': msg,
                    }
            else:
                msg = "You must sign in as a bidder to place a bid!"
                context = {
                    'product': product,
                    'msg': msg,
                }
        else:
            msg = "Please, sign in as bidder to place a bid!"
            context = {
                'product': product,
                'msg': msg,
            }
    return render(request, 'auction/auction.html',context)


# ....API....

def registration(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        usertype = request.POST.get('usertype')

        userexists = User.objects.filter(username = username)
        if usertype == "Buyer" or usertype == "Seller":
            if pass1 == pass2:
                if len(userexists) == 0:
                    user =  User.objects.create_user(username,email,pass1)
                    user.first_name = fname
                    user.last_name = usertype
                    user.save()
                    messages.success(request, "Account created successfully!")
                    return redirect('login')
                else:
                    messages.error(request, "Username already exists!!")
            else:
                messages.error(request, "Passwords don't match!!")
        else:
            messages.error(request, "Must select User Type!!")

    context = {
    }
    return render(request, 'auction/registration.html', context)


def signin(request):
    context = {
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            request.session['usertype'] = request.user.last_name
            messages.success(request, "Sign In successful!")
            return redirect('home')
        else:
            messages.error(request, "Username or password incorrect!!")
    return render(request, 'auction/login.html', context)

def signout(request):
    logout(request)
    return redirect('home')


def dashboard(request):
    context = {
    }
    
    return render(request, 'auction/seller_dashboard.html', context)


def profile(request):
    context = {
    }
    
    return render(request, 'auction/profile.html', context)