from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArticleTopic(models.Model):
	text = models.CharField(max_length=40, unique=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.text

class ArticleEntry(models.Model):
	# Creating one to one relation
	topic = models.OneToOneField(ArticleTopic, on_delete=models.CASCADE,
		primary_key=True)
	
	article = models.TextField(max_length=1000)

	def __str__(self):
		return self.article