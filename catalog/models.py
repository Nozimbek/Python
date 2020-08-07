from django.db import models

class Movie(models.Model):
    name = models.CharField('name', max_length=255)
    description = models.TextField('description')
    poster = models.ImageField(upload_to='posters')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    available_seats = models.IntegerField()

    def __str__(self):
        return self.name

