from django.contrib import admin
from .models import Gust, Movie, Reservation
# Register your models here.

admin.site.register(Gust)
admin.site.register(Movie)
admin.site.register(Reservation)
