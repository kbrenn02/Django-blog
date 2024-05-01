from django.urls import path
from . import views

urlpatterns = [
    path("", views.article_list), #as this is the homepage, there is no route/url path to take so the string is empty
]
