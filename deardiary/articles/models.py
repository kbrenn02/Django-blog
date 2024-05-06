from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)  # each of these are columns in the db/elements of the article. Need to set them equal to their Field type
    slug = models.SlugField()  # Slug is a URL
    body = models.TextField()  
    date = models.DateTimeField(auto_now_add=True)  # when an article is created, the time is automatically generated  
    # later add: thumbnail, author
    thumb = models.ImageField(default='default.png', blank=True)
    # later add: author. Have to use a foreign key, and to do that, have to import User above
    author = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):  # added this so that when we work in the shell environmnet, we see the title of the article objects we create
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'