from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieSearchForm, ReviewForm
import requests

class MoviePages:
    def __init__(self):
        self.movie_view = {}

    def getMovie(self, title):
        api_key = '2f0e70a3'
        response =  requests.get(f'http://www.omdbapi.com/?apikey={api_key}&t={title}')
    
        if response.status_code == 200:
            data_movie = response.json()
            return {
                'poster': data_movie.get('Poster'),
                'title': data_movie.get('Title'),
                'type': data_movie.get('Type'),
                'release': data_movie.get('Released'),
                'plot': data_movie.get('Plot'),
                'language': data_movie.get('Language'),
                'genre': data_movie.get('Genre'),
                'director': data_movie.get('Director'),
                'writer': data_movie.get('Writer'),
                'actors': data_movie.get('Actors'),
                'awards': data_movie.get('Awards')
            }
        return None

    def fetchMovieData(self, request):
        search_form = MovieSearchForm(request.GET or None) 
        review_form = ReviewForm(request.POST or None)
    
        if search_form.is_valid():
            title = search_form.cleaned_data['title']
            self.movie_view = self.getMovie(title)
            
    
        if review_form.is_valid() and 'title' in search_form.cleaned_data:
            review_data = review_form.cleaned_data
            movie, created = Movie.objects.update_or_create(
                title=search_form.cleaned_data['title'],
                defaults={
                    'userName': review_data['userName'],
                    'userRating': review_data['userRating'],
                    'userReview': review_data['userReview']
                }
            )
            
            return redirect('fetch_movie_data')
    
        return render(request, 'index.html', {
            'search_form': search_form, 
            'review_form': review_form, 
            'movie_view': self.movie_view
        })
    
    
    def reviewList(self, request):
        reviews = Movie.objects.all()
        return render(request, 'review_list.html', {'reviews': reviews})
    
    def reviewDetail(self, request, id):
        review = get_object_or_404(Movie, id = id)
        
        movie_view = self.getMovie(review.title)

        return render(request, 'review_detail.html', {'review' : review, 'movie_view' : movie_view})
    
    def reviewEdit(self, request, id=None):
        review = get_object_or_404(Movie, id=id)
        
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review.userName = form.cleaned_data['userName']
                review.userRating = form.cleaned_data['userRating']
                review.userReview = form.cleaned_data['userReview']
                review.save()
                return redirect('review_list')
        else:
            form = ReviewForm(initial={
                'userName': review.userName,
                'userRating': review.userRating,
                'userReview': review.userReview
            })
        
        return render(request, 'review_edit.html', {'form': form, 'review': review})
    
    def reviewDelete(self, request, id):
        review = get_object_or_404(Movie, id=id)
        movie_view = self.getMovie(review.title)
    
        if request.method == 'POST':
            review.delete()
            return redirect('review_list') 
    
        return render(request, 'review_confirm_delete.html', {'review': review, 'movie_view' : movie_view})