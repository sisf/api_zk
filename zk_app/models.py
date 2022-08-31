from django.db import models

# Create your models here.

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    date = models.DateField()
    
    
class Gust(models.Model):
    name = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    
    
class Reservation(models.Model):
    gust = models.ForeignKey(Gust, related_name='reservation', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE)
    
