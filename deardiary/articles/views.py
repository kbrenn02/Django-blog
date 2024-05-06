from django.shortcuts import render, redirect;
from .models import Article;
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')  #this grabs all records from article db table. Can order by any field in the model
    return render(request, 'articles/article_list.html', { 'articles': articles })  #the third parameter is the data we want to send to the template

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required(login_url='/accounts/login/') #this protects the article_create view
def article_create(request):
    if request.method == 'POST':
        # when we upload files, they don't come as part of the POST object, they come on the FILES object on the request itself
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            # we have access to the user on the request (because the user made the request), so we can grab that user
            instance.author = request.user
            instance.save() #this saves the instance with the article
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    # if we want to send data to be used in the html template, we have to add the third parameter
    return render(request, 'articles/article_create.html', {'form':form})