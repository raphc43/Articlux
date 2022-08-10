# Serializer class
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ArticleTopic

# class to represent all registered usernames in json format
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'id')

class TopicSerializer(serializers.ModelSerializer):
	class Meta:
		model = ArticleTopic
		fields = '__all__'