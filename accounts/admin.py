from django.contrib import admin
from community.models import Article
from movies.models import Movie
from .models import User

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display=('pk', 'title', 'content', 'created_at', 'updated_at',)

class MovieAdmin(admin.ModelAdmin):
	list_display="__all__"

class UserAdmin(admin.ModelAdmin):
	list_display="__all__"

admin.site.register(Article)
admin.site.register(Movie)
admin.site.register(User)