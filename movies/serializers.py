# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from movies.models import Movie, Comment

# User = get_user_model()

# class CommentSerializer(serializers.ModelSerializer):
    
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ('pk', 'username')

#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Comment
#         fields = ('pk', 'user', 'content', 'movie',)
#         read_only_fields = ('movie', )


# class MovieSerializer(serializers.ModelSerializer):
    
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ('pk', 'username')

#     user = UserSerializer(read_only=True)
#     like_users = UserSerializer(read_only=True, many=True)
#     comments = CommentSerializer(many=True, read_only=True)

#     class Meta:
#         model = Movie
#         fields = '__all__'

# class MovieListSerializer(serializers.ModelSerializer):
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ('pk', 'username')

#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Movie
#         fields = ('pk', 'user', 'title', 'poster_path',)
