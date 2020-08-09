from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    item_name = models.CharField(max_length=255)
    item_desc = models.TextField()
    bid_start = models.FloatField()
    image = models.CharField(max_length=255, blank=True)
    item_category = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name}"
