from django.contrib import admin
from .models import Products,Auction
# Register your models here.

class productsAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_desc','current_val','start_time','end_time','product_img')

admin.site.register(Products,productsAdmin)

class auctionAdmin(admin.ModelAdmin):
    list_display = ('product','user','last_bid_val','last_bid_time')

admin.site.register(Auction,auctionAdmin)