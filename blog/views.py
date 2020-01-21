'''뷰(view)는 애플리케이션의 "로직"을 넣는 곳이에요. 뷰는 이전 장에서 만들었던 모델에서 필요한 정보를 받아와서 템플릿에 전달하는 역할을 합니다. '''
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return  render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
