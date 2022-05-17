from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # movies
    path('', views.movie_list_or_create),
    path('<int:movie_pk>/', views.movie_detail_or_update_or_delete),
    path('<int:movie_pk>/like/', views.like_movie),

]
