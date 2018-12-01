"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# the url function is not used like in the book, path is used instead due to url not working
# from django.conf.urls import include, urls for some reason urls could not be imported
app_name = 'learning_logs'
urlpatterns = [
	# the path below does not uses include like in the book
    path('admin/', admin.site.urls),
    # the path below does not have namespace like the book
    path('', include('learning_logs.urls')),
]
