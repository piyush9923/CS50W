from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"


class AuctionListing(models.Model):
    item_name = models.CharField(max_length=255)
    item_desc = models.TextField()
    bid_start = models.FloatField()
    image = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, related_name='item_cat', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name}"


class Bidding(models.Model):
    bid_item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    post_bid = models.FloatField()

    def __str__(self):
        return f"Updated bid for {self.bid_item.item_name} of {self.post_bid}"


class Comments(models.Model):
    comment_item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    post_comment = models.TextField()

    def __str__(self):
        return f"Comment added for {self.comment_item}"
