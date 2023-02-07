from django.db import models
from auction.models import Auction
from django.contrib.auth.models import User
# Create your models here.

# class Cart(models.Model):
#     auction = models.ForeignKey(Auction , on_delete=models.CASCADE)
#     user = models.ForeignKey(User , on_delete=models.CASCADE)
#     price = models.CharField(max_length=14)
