from django.forms import ModelForm
from .models import Task, TaskGroup

class TaskGroupForm(ModelForm):
	class Meta:
		model = TaskGroup
		fields = ['name',]


class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'description', 'priority']
