from django.shortcuts import get_list_or_404, render, redirect
from .models import Movie
# Create your views here.
def movie_list(request):
    movies = Movie.objects.order_by('pk')
    context  = {
        'movies' : movies
    }
    print(movies)
    return render(request, 'movies/index.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie,
    }
    return render(request, 'movies/detail.html', context)