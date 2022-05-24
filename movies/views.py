import random
from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Movie, MovieComment
from .forms import MovieCommentForm
from django_pandas.io import read_frame
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy.linalg import norm
import numpy as np

# Create your views here.
def movie_list(request):
    movies = Movie.objects.order_by('pk')
    context  = {
        'movies' : movies
    }

    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = MovieCommentForm()
    comments=movie.moviecomment_set.all()
    context = {
        'movie' : movie,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'movies/detail.html', context)

def comments_create(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        comment_form = MovieCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')

def comments_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        comment=get_object_or_404(MovieComment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail', movie_pk)

def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user) # 좋아요 취소
        else:   # 없다면 좋아요 하기
            movie.like_users.add(request.user)
        return redirect('movies:detail', movie_pk)

def recommend(request, username):
    movies = Movie.objects.all()
    data = read_frame(movies)
    data["overview"].isnull().sum()
    data['overview']=data['overview'].fillna('')
    data['overview'].isnull().sum()

    tfidf=TfidfVectorizer()
    tfidf_mat=tfidf.fit_transform(data['overview']).toarray()
    def cos_sim2(X, Y):
        return np.dot(X, Y)/((norm(X)*norm(Y))+ 1e-7)

    def top_match_ar2(data, name, rank=5, simf=cos_sim2):
        sim=[]
        for i in range(len(data)):
            if name != i:
                sim.append((simf(data[i], data[name]), i))
        sim.sort()
        sim.reverse()
        return sim[:rank]

    person = get_object_or_404(get_user_model(), username=username)
    movielist  = person.like_movies.all()
    movielst  = person.movie_comments.all()
    idx = []
    maxLst = []
    movieLst = []
    if len(movielst) != 0:
        for movie in movielst:
            maxLst.append(movie.rank)
        
        for movie in movielst:
            if max(maxLst) == movie.rank:
                idx.append(movie.id)

        num2 = random.choice(idx)

        for sim, movie_id in top_match_ar2(tfidf_mat, num2, 10):
            movieLst.append((data.loc[movie_id, ['id', 'title', 'poster_path']]))
        movieLst = movieLst[:5]

    movieList = []
    if len(movielist) != 0:
        rc = []
        for i in movielist:
            rc.append(i.id)
        num = random.choice(rc)

        for sim, movie_id in top_match_ar2(tfidf_mat, num, 10):
            movieList.append((data.loc[movie_id, ['id', 'title', 'poster_path']]))
        movieList = movieList[:5]

    context = {
        'movieLst':movieLst,
        'movieList':movieList,
    }
    return render(request, 'movies/recommend.html', context)

def recommend2(request, username):
    movies = Movie.objects.all()
    data = read_frame(movies)
    data["overview"].isnull().sum()
    data['overview']=data['overview'].fillna('')
    data['overview'].isnull().sum()

    tfidf=TfidfVectorizer()
    tfidf_mat=tfidf.fit_transform(data['overview']).toarray()
    def cos_sim2(X, Y):
        return np.dot(X, Y)/((norm(X)*norm(Y))+ 1e-7)

    def top_match_ar2(data, name, rank=5, simf=cos_sim2):
        sim=[]
        for i in range(len(data)):
            if name != i:
                sim.append((simf(data[i], data[name]), i))
        sim.sort()
        sim.reverse()
        return sim[:rank]

    person = get_object_or_404(get_user_model(), username=username)
    movielist  = person.movie_comments.all()
    maxV = 0
    for movie in movielist:
        if maxV < movie.rank:
            idx = movie.id

    num = idx

    movieList = []
    for sim, movie_id in top_match_ar2(tfidf_mat, num, 10):
        movieList.append((data.loc[movie_id, ['id', 'title', 'poster_path']]))
    movieList = movieList[:10]

    context = {
        'movieList':movieList
    }
    return render(request, 'movies/recommend.html', context)