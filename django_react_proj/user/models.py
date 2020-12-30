from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=100, default='')
    Password = models.CharField(max_length=40)

    Viewed = models.CharField(max_length=1000, default='')
    PlanToWatch = models.CharField(max_length=1000, default='')
    Dropped = models.CharField(max_length=1000, default='')


    def __str__(self):
        return self.Username