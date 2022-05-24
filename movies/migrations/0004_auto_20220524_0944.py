# Generated by Django 3.2.7 on 2022-05-24 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_auto_20220524_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecomment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_comments', to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='moviecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]