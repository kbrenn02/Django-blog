from django.shortcuts import render;
from .models import Article;

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')  #this grabs all records from article db table. Can order by any field in the model
    return render(request, 'articles/article_list.html', { 'articles': articles })  #the third parameter is the data we want to send to the template