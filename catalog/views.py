from django.shortcuts import render, redirect
from .models import Movie, Booking, MoviePlay
import random
from .forms import NameForm

def index(request):

    search_query = request.GET.get('search', None)
    if search_query:
        movies = Movie.objects.filter(name__icontains=search_query)
    else:
        movies = Movie.objects.all()
    return render(request, 'index.html', { 'movies': movies})


def about(request):
    return render(request, 'about.html')


def movie_details(request, movie_pk):
    try:
        movie = Movie.objects.get(pk=movie_pk)
        return render(request, 'movie_details.html', {'movie': movie})
    except Movie.DoesNotExist:
        return redirect('Home')




def movie_play_details(request, movie_play_pk):
    
    if request.method == 'GET':
        movie_book = MoviePlay.objects.get(pk=movie_play_pk)
        random_key = random.random()
        return render(request, 'movie_play_details.html', {'random_key': random_key})
    else:
        form = NameForm(request.POST)
        if form.is_valid():
            Booking.client_name = NameForm.client_name
            Booking.secret_number = random_key
            return HttpResponseRedirect('thanks')
           

def booked(request, movie_play_pk):
    return render(request, 'thanks.html')
