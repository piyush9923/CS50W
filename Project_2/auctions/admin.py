from django.contrib import admin
from .models import Category, AuctionListing, Bidding, Comments

# Register your models here.
admin.site.register(Category)
admin.site.register(AuctionListing)
admin.site.register(Bidding)
admin.site.register(Comments)