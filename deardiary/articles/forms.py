from django import forms
from . import models

class CreateArticle(forms.ModelForm): #similar to UserCreationForm and AuthenticationForm in views.py in accounts
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']