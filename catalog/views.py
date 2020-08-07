from django.shortcuts import render, redirect
from .models import Movie, Booking, MoviePlay

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


