from django import forms
from .models import Posting, Comment

class PostingModelForm(forms.ModelForm):  # data의 입력과 검증 & HTML 
    content = forms.CharField(min_length=2)
    
    class Meta:
        model = Posting
        widget = {
            'content': forms.Textarea(attrs={
                'col': 80,
                'row': 20,
                'class': 'hi byes'
            })
        }
        fields = ('content', 'image', 'icon')


class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)

    class Meta:
        model = Comment
        fields = ('content',)