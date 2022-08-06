from django.contrib import admin
from .models import ArticleTopic, ArticleEntry

# Register your models here.
admin.site.register(ArticleTopic)
admin.site.register(ArticleEntry)