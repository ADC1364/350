# Defines URL patterns for learning_logs.
from django.urls import path
from . import views
# from django.conf.urls import url, which is from the book did not work for some reason, so I had to use path instead

app_name= 'learning_logs'

urlpatterns = [
	#Home page
	path('', views.index, name='index'),
	
	# Show all Topics
	path('topics/', views.topics, name='topics'),
]
