from django.db import models

class Movie(models.Model):
    name = models.CharField('name', max_length=255)
    description = models.TextField('description')
    poster = models.ImageField(upload_to='posters')


    def __str__(self):
        return self.name

class MoviePlay(models.Model):
    belongs_to = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='slots')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    available_seats = models.IntegerField()

class Booking(models.Model):
    for_slot = models.ForeignKey(MoviePlay, on_delete=models.CASCADE, related_name='bookings')
    client_name = models.CharField(max_length=255)
    secret_number = models.CharField(max_length=255)