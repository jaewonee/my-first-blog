from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #장고에게 누군가 웹사이트에 'http://127.0.0.1:8000/' 주소로 들어왔을 때 views.post_list를 보여주라고 말해줍니다.
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #장고는 정수 값을 기대하고 이를 pk라는 변수로 뷰로 전송하는 것을 말합니다.
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]