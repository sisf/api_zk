from django.contrib import admin
from .models import Gust, Movie, Reservation, Music
# Register your models here.

admin.site.register(Gust)
admin.site.register(Movie)
admin.site.register(Reservation)
admin.site.register(Music)
