from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
	path('', views.home, name='home'),
	path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),
	path('register/', views.register_user, name='register'),
	path('profile/', views.profile, name='profile'),
]