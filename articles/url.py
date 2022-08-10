from django.urls import path
from .views import ArticlesView, ArticleView, AddTopic, Home, rest_users, rest_topics

app_name = 'articles'

# Defining url patterns
urlpatterns = [
    path('articles/', ArticlesView, name='articles_page'),
    path('article/<int:topic_id>/', ArticleView, name='article_page'),
    path('add/topic/', AddTopic, name='add_topic'),
    path('', Home, name='home_page'),
    path('rest/', rest_users, name="rest_service"),
    path('rest/<int:user_id>', rest_topics, name="rest_service"),
]