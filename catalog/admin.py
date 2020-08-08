from django.contrib import admin
from .models import Movie, MoviePlay, Booking

admin.site.register(Movie)
admin.site.register(MoviePlay)
admin.site.register(Booking)
