from django import forms
from .models import Topic, Entry



class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		# I added priority
		fields =['text', 'priority']
		labels = {'text': '', 'priority': ''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text', 'status']
		labels = {'text': '', 'status': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
		
		
