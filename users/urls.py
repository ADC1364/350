# defines URL patterns for users

from django.urls import re_path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
	# Login page
	re_path(r'^login/$',LoginView.as_view(template_name='users/login.html'), name='login'),
	
	#Logout page, creating our own view
	re_path(r'^logout/$', views.logout_view, name='logout'),
	]
