from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)  # each of these are columns in the db/elements of the article. Need to set them equal to their Field type
    slug = models.SlugField()  # Slug is a URL
    body = models.TextField()  
    date = models.DateTimeField(auto_now_add=True)  # when an article is created, the time is automatically generated  
    # later add: thumbnail, author
    # thumbnail = models.ImageField
    # author = models.CharField