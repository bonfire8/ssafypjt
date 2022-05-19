from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # movies
    path('', views.movie_list, name='index'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    # path('<int:movie_pk>/like/', views.like_movie),

]
