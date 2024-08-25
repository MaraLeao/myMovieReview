from django.urls import path
from .views import MoviePages

pages = MoviePages()

urlpatterns = [
    path('', pages.fetchMovieData, name='home'), 
    path('fetch-movie/', pages.fetchMovieData, name = 'fetch_movie_data' ),
    path('reviews/', pages.reviewList, name='review_list'),
    path('reviews/<int:id>/', pages.reviewDetail, name='review_detail'),
    path('reviews/<int:id>/edit/', pages.reviewEdit, name='review_edit'),
    path('reviews/<int:id>/delete/', pages.reviewDelete, name='review_confirm_delete')
]