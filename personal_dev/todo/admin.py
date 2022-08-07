from django.contrib import admin
from . import models



admin.site.register(models.TaskGroup)
admin.site.register(models.Task)