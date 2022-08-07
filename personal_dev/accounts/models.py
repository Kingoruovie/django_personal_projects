from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profile_pic = models.ImageField(default='default.jpg')

	def __str__(self):
		return f'{self.user.username} profile'
