from django.shortcuts import render, redirect

# Create your views here.
def movie_list_or_create(request):
    return render(request, 'movies/index.html')