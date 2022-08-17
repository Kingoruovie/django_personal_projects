from django.db import models


class Project(models.Model):
	image = models.ImageField()
	title = models.CharField(max_length=100)
	technology = models.CharField(max_length=200)
	description = models.TextField()
	github_url = models.URLField(max_length=200)

	def __str__(self):
		return self.title

	def snippet(self):
		return f'{self.description[:50]} ...' 
