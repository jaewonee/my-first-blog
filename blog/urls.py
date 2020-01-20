from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #장고에게 누군가 웹사이트에 'http://127.0.0.1:8000/' 주소로 들어왔을 때 views.post_list를 보여주라고 말해줍니다.
    
]