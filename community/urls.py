from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    # community
    path('', views.index, name='index'),
    path('create/', views.create, name='create'), # GET / POST
    # path('<int:article_pk>/', views.article_detail, name='detail'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'), # GET / POST
    path('<int:article_pk>/like/', views.likes, name='likes'),
    
    # comments
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
