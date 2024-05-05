from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path("", views.article_list, name="list"), #as this is the homepage, there is no route/url path to take so the string is empty
    path('create/', views.article_create, name='create'),
    path(r'<slug:slug>/', views.article_detail, name="detail"), #we've captured where the user wants to go to
]
