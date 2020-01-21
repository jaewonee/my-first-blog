'''로컬 컴퓨터와 PythonAnywhere의 데이터베이스는 동기화되지 않습니다.'''
from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #다른 모델에 대한 링크
    title = models.CharField(max_length=200) #글자수 제한 있음
    text = models.TextField() #글자수 제한 없음
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title