from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # movies
    path('', views.movie_list, name='index'),
    path('<int:movie_pk>/detail/', views.detail, name='detail'),
    path('<int:movie_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
    path('recommend/<username>/' ,views.recommend, name='recommend'),
    path('<int:movie_pk>/unlikes/', views.unlikes, name='unlikes'),
    path('<int:movie_pk>/comments/<int:comment_pk>/update/', views.comments_update, name='comments_update'),


]
