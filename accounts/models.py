from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.CharField()
    sex = models.BooleanField(default=False) # 성별 체크 위젯 만들기(기본값 false)
    pass
