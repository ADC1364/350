# Defines URL patterns for learning_logs.
from django.urls import path
from . import views
# from django.conf.urls import url, which is from the book did not work for some reason, so I had to use path instead

app_name = 'learning_logs'

urlpatterns = [
	#Home page
	path('', views.index, name='index'),
	
	# Show all Topics
	path('topics/', views.topics, name= 'topics'),
	
	# Detail Page for a single Topic
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	
	
	# Page for adding a new topic
	path('new_topic/', views.new_topic, name='new_topic'),
	
	# Page for adding a new entry
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	
	# Page for editing an entry
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
