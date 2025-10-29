from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all() #DB의 모든 게시글 가져오기
    
    return render(request, 'posts/post_list.html', {'posts':posts})