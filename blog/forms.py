from django import forms
from .models import Post

'''
PostForm: 우리가 만들 폼의 이름
form.ModelForm: 장고에 이 폼이 ModelForm이라고 알려줌
 class Meta: model = Post :폼을 만들기 위해서 필요한 model 명시
 
'''

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')