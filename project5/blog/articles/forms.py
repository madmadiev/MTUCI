from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Article.objects.filter(title=title).exists():
            raise forms.ValidationError("Статья с таким названием уже существует.")
        return title