from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    placeid = models.CharField(max_length=100, default='')
    eventid = models.CharField(max_length=60)
    aboutid = models.TextField()
    date = models.DateTimeField()
    EntryFeeid = models.IntegerField()
    categoryid = models.CharField(max_length=20)


class user_det(models.Model):
    user_ids = models.IntegerField()
    phoneno = models.CharField(max_length=10)


class admins(models.Model):
    username = models.CharField(max_length=20, default="admin")
    password = models.CharField(max_length=15, default="1234")


class Booking(models.Model):
    name = models.CharField(max_length=100)
    nos = models.IntegerField()
    Evnt_id = models.CharField(max_length=300)
    total = models.IntegerField(default='')
    uuser = models.ForeignKey(User, on_delete=models.CASCADE)
    date_now = models.DateTimeField(auto_now=True)

# class Paymentt(models.Model):
#     fname=models.CharField(max_length=100)
#     eemail=models.EmailField()
#     namec=models.CharField(max_length=30)
#     NoC=models.CharField(max_length=25)
#     exp=models.CharField(max_length=30)
#     expyear=models.CharField(max_length=10)
#     cvv=models.IntegerField()
