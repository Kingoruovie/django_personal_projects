from django.forms import ModelForm
from .models import Task, TaskGroup
from django import forms

class TaskGroupForm(ModelForm):
	name = forms.CharField(required=False, max_length=100)
	class Meta:
		model = TaskGroup
		fields = ['name',]


class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'description', 'priority']
