from rest_framework import serializers
from django.contrib.auth import get_user_model
from reviews.models import Review

class ProfileSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Review
            fields = ('pk', 'title', 'content')

    like_articles = ReviewSerializer(many=True)
    articles = ReviewSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_articles', 'articles',)

