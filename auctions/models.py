from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    pass

class listing(models.Model):
    user_id = models.IntegerField()
    item_name = models.CharField(max_length = 50)
    item_img = CloudinaryField('image')
    item_description = models.TextField()
    item_price = models.FloatField(default = 1)
    date_posted = models.DateField(auto_now_add = True, blank = True)
    status = models.CharField(default = "Active", max_length = 10)
    winner_id = models.IntegerField(default = 0)
    category = models.CharField(max_length = 15, blank = True)
    File = CloudinaryField('raw')

class bid(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length = 64)
    item_id = models.IntegerField()
    bid_amount = models.FloatField()
    bid_date = models.DateTimeField(auto_now = True, blank = True)

class comment(models.Model):
    username = models.CharField(max_length = 64)
    item_id = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add = True, blank = True)

class watchlist(models.Model):
    user_id = models.IntegerField()
    item_id = models.IntegerField()

class sale(models.Model):
    buyer_id = models.IntegerField()
    buyer_username = models.CharField(max_length = 64)
    item_id = models.IntegerField()