from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	
	# A topic the user is learning about
	text = models.TextField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
	#  I added priority to the topic
	HIGH= 'high'
	MEDIUM= 'medium'
	LOW= 'low'
	PRIORITY_CHOICES = (
	(HIGH, 'high'),
	(MEDIUM, 'medium'),
	(LOW, 'low'),
	)
	priority = models.CharField(max_length=6,choices=PRIORITY_CHOICES, default=MEDIUM,)
	
	
	def __str__(self):
		# Return a string representation of the model
		return self.text

class Entry(models.Model):
	# Something specific learned about a topic
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	#  I added status to each entry
	COMPLETE= 'complete'
	INCOMPLETE= 'incomplete'
	STATUS_CHOICES = (
	(COMPLETE, 'complete'),
	(INCOMPLETE, 'incomplete'),
	)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES, default=INCOMPLETE,)
	
	class Meta:
		verbose_name_plural = 'entries'
	
	def __str__(self):
		# Return a string representation of the model
		return self.text[:50] + "..."
