from django.shortcuts import render

# Create your views here.
from .models import ArticleTopic, ArticleEntry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
import json
from django.contrib.auth.models import User


from .serializers import UserSerializer, TopicSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
@api_view(['GET'])
def rest_users(request):
	if request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def rest_topics(request, user_id):
	if request.method == 'GET':
		user = User.objects.get(id=user_id)
		topics = ArticleTopic.objects.filter(user=user)
		serializer = TopicSerializer(topics, many=True)
		return Response(serializer.data)



def Home(request):
	return render(request, 'home.html')

@login_required
def ArticlesView(request):
	topics = ArticleTopic.objects.filter(user=request.user)
	context = {'topics': topics}
	return render(request, 'articles.html', context)

@login_required
def ArticleView(request, topic_id):
	topic = ArticleTopic.objects.get(id=topic_id)
	if topic.user != request.user:
		raise Http404

	# Accessing related entry by assigning topic field a topic instance
	try:
		entry = ArticleEntry.objects.get(topic=topic)
	except:
		entry=False
	else:
		pass
		
	# If no entry then create and handle form
	if request.method == 'POST':
		form = EntryForm(request.POST)

		if form.is_valid():
			form.instance.topic = topic
			form.save()
			#return HttpResponseRedirect(f'http://localhost:8000/article/{topic_id}')
	else:
		form = EntryForm()

	context = {'topic': topic, 'entry': entry, 'form': form}
	return render(request, 'article.html', context)

@login_required
def AddTopic(request):
	"""View to create topics"""
	if request.method == 'POST':
		form = TopicForm(request.POST)

		if form.is_valid():
			form.instance.user = request.user
			form.save()
			return HttpResponseRedirect('http://localhost:8000/articles/')
	else:
		form = TopicForm()

	context = {'form': form}
	return render(request, 'add_topic.html', context)