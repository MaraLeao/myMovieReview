from django.shortcuts import render
from .models import Movie
import requests
from .forms import MovieForm

def fetchMovieData(request):
    movie = None
    form = MovieForm(request.GET or None)
    api_key = '2f0e70a3'

    if form.is_valid():
        title = form.cleaned_data['title']
        response = requests.get(f'http://www.omdbapi.com/?apikey={api_key}&t={title}')

        if response.status_code == 200:
            data_movie = response.json()
            movie = Movie.objects.create(
                title = title,
                type = data_movie.get('type'),
                year = data_movie.get('y'),
                plot = data_movie.get('plot')
            )
    
    return render(request, 'index.html', {'form' : form, 'movie': movie})