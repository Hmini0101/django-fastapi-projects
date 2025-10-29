from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # post/ 경로에 접속하면 views.post.list 함수 실행
    path('', views.post_list, name='list'),
]