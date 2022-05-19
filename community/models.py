# from django.db import models
# from django.conf import settings

# # Create your models here.
# class Article(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.TextField()
#     content = models.CharField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Comment(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
#     content = models.CharField(max_length=200)
