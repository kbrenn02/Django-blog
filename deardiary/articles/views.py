from django.shortcuts import render;
from .models import Article;
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')  #this grabs all records from article db table. Can order by any field in the model
    return render(request, 'articles/article_list.html', { 'articles': articles })  #the third parameter is the data we want to send to the template

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required(login_url='/accounts/login/') #this protects the article_create view
def article_create(request):
    return render(request, 'articles/article_create.html')