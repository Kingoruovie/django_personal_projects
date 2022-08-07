from django.db import models
from django.contrib.auth.models import User



class TaskGroup(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, default='')
	date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(max_length=200, default='')

	def __str__(self):
		return self.name


class Task(models.Model):

	priority = [
		('A', 'MUST DO'),
		('B', 'SHOULD DO'),
		('C', 'WANT TO DO'),
	]

	title = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=False)
	priority = models.CharField(max_length=1, choices=priority)
	group = models.ForeignKey(TaskGroup, on_delete=models.CASCADE)

	def __str__(self):
		return self.title	
