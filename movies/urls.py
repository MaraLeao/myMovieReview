from django.urls import path
from .views import fetchMovieData

urlpatterns = [
    path('', fetchMovieData, name='home'),  # Adiciona a URL raiz
    path('fetch-movie/', fetchMovieData, name = 'fetch_movie_data' )
]