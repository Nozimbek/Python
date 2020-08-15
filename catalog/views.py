from django.shortcuts import render, redirect
from .models import Movie, Booking, MoviePlay
import random
from .forms import BookingForm, CheckingForm

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
    try:
            movie_play = MoviePlay.objects.get(pk=movie_play_pk)
    except MoviePlay.DoesNotExist:
        return redirect('Home')

    if request.method == 'GET':
        booking_form = BookingForm()
        return render(request, 'movie_play_details.html', {'booking_form': booking_form})
    else:
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.for_slot = movie_play
            booking.secret_number = random.randint(1000, 9999)
            booking.save()
            return render(request, 'booking_done.html', {'booking': booking})
        else:
            return render(request, 'movie_play_details.html', {'booking_form': booking_form})


def check(request):
    if request.method == 'GET':
        checking_form = CheckingForm()
        return render(request, 'checking_details.html', {'checking_form': checking_form})
    else:
        checking_form = CheckingForm(request.POST)
        if checking_form.is_valid():
            secret_number = Booking.objects.filter(secret_number=checking_form.cleaned_data['secret_number'])
            return render(request, 'checking_done.html', {'secret_number': secret_number})
        else:
            redirect(movie_play_details.html)



