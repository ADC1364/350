# Defines URL patterns for learning_logs.
from django.urls import re_path
from . import views
# from django.conf.urls import url, which is from the book did not work for some reason, so I had to use path instead

app_name = 'learning_logs'

urlpatterns = [
	#Home page
	re_path(r'^$', views.index, name='index'),
	
	# Show all Topics
	re_path(r'^topics/$', views.topics, name= 'topics'),
	
	# Detail Page for a single Topic
	re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	
	
	# Page for adding a new topic
	re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
	
	# Page for adding a new entry
	re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	
	# Page for editing an entry
	re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
