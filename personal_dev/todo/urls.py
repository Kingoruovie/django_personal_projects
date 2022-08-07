from django.urls import path
from . import views


app_name='todo'
urlpatterns = [
	path('', views.homepage, name='homegroup_list'), # All the groups or todo created by a particular user.
	path('group/create', views.group_create, name='group_create'),
	path('group/delete/<int:pk>/', views.group_delete, name='group_delete'),
	path('group/update/<int:pk>/', views.group_update, name='group_update'),
	path('group/<int:pk>/', views.group_detail, name='group_detail'),

	
	path('task/<int:pk>/', views.task_detail, name='task_detail'),
	path('task/create/<int:pk>', views.task_create, name='task_create'),
	path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
	path('task/update/<int:pk>/', views.task_update, name='task_update'),

	path('task/mark/<int:pk>/', views.task_completeness, name='task_tick'),
]