from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):  #클래스 이름 항상 대문자
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #문자 수가 제한되어 있는 텍스트 정의
    text = models.TextField()#제한이 없는 긴 텍스트
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #메소드
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title