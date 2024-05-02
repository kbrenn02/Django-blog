from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)  #admin.site.register is how we tell the admin portal that we're registering a model