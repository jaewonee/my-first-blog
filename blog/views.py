'''뷰(view)는 애플리케이션의 "로직"을 넣는 곳이에요. 뷰는 이전 장에서 만들었던 모델에서 필요한 정보를 받아와서 템플릿에 전달하는 역할을 합니다. '''
from django.shortcuts import render

# Create your views here.

def post_list(request):
    return  render(request, 'blog/post_list.html',{})