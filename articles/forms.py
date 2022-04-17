from genericpath import exists
from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title' , 'content']
    
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.all().filter(title__icontains=title)
        if qs.exists():
            self.add_error("Title", f"{title}  is already in use.")

        return data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        return cleaned_data