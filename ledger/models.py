import datetime

from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=60)
    balance = models.FloatField(default=0)
    founded = models.DateTimeField('date founded')

    def __str__(self):
        return self.user_name

class Program(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    detail = models.CharField(max_length=100)
    value = models.FloatField(default=0)
    date = models.DateField(default=datetime.date.today)
    type_of_programe = models.CharField(max_length=1, default="I")

    def __str__(self):
        return self.detail
    
