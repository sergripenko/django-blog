from django import forms
from .models import Comments, Post


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['massage']


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows':"2"}),
            }

        labels = {
            'title': 'Заголовок поста',
            'text': 'Основной текст поста',
        }