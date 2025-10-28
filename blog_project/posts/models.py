from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 객체가 생성될때 자동으로 현재 시간 저장
    updated_at = models.DateTimeField(auto_now=True) # 객체가 저장될때마다 자동으로 시간 갱신
    
    def __str__(self):
        #객체를 문자열로 표시하는 메서드
        return self.title
    
    class Meta:
        #게시글 목록을 최신순으로 정렬하도록 설정
        ordering = ['-created_at']