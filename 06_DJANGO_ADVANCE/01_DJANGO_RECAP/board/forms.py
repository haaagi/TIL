from django import forms
from .models import Article, Comment

# forms.Form => data 입력 및 검증
# forms.ModelForm => Data 입력/ 검증 + html 생성


class ArticleModelForm(forms.ModelForm):
    # 1. Data 입력 및 검증
    # 2. HTML 생성
    title = forms.CharField(min_length=2, max_length=100, required=False)
    class Meta:
        model = Article
        fields = '__all__'


class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)  # forms.py의 max_length는 200 이넘어가면 에러뜬다. but models.py 에 쓴거는 200넘어가면 200자까지만 저장한다는 뜻

    class Meta:
        model = Comment
        fields = '__all__'