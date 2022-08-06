from django import forms
from .models import ArticleTopic, ArticleEntry

class TopicForm(forms.ModelForm):
	"""Form to create articles"""
	class Meta:
		model = ArticleTopic
		fields = '__all__'
		labels = {
			'text': 'Create a topic'
		}

class EntryForm(forms.ModelForm):
	"""Form to create articles"""
	class Meta:
		model = ArticleEntry
		fields = ('article',)
		labels = {
			'article': 'Write an article'
		}