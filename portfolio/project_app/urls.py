from django.urls import path
from . import views

app_name='project_app'
urlpatterns =[
	path('', views.home, name='home'),
	path('resume/', views.resume, name='resume'),
	path('projects/', views.all_project, name='all_project'),
	path('projects/<int:pk>', views.project_detail, name='project_detail'),
]