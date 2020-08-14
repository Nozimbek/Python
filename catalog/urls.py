from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="Home"),
    path('About', views.about, name="About"),
    path('movies/<int:movie_pk>/', views.movie_details, name='show_movie_details'),
    path('movieplay/<int:movie_play_pk>/', views.movie_play_details, name='movie_play_details'),
    path('check', views.check, name="checking"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
