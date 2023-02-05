from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=50)
    current_val = models.CharField(max_length=14)
    product_desc = models.TextField()
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank = False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank = False)
    product_img = models.ImageField(upload_to='auction/images/', blank = True)


class Auction(models.Model):
    product = models.ForeignKey(Products , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    last_bid_val = models.CharField(max_length=14)
    last_bid_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank = True)
