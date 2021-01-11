from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=100, default='')

    Viewed = models.CharField(max_length=1000, blank=True, default='')
    PlanToWatch = models.CharField(max_length=1000, blank=True,default='')
    Dropped = models.CharField(max_length=1000, blank=True, default='')


    def __str__(self):
        return self.Username