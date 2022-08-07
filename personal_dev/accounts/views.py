from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request, 'accounts/base.html')


def login_user(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			if 'next' in request.POST:
				print(request.POST.get('next'))
				return redirect(request.POST.get('next'))
			else:
				return redirect('accounts:home')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login_form.html', {'form': form})



def logout_user(request):
	if request.method == 'POST':
		logout(request)
		return redirect('accounts:login')
	else:
		return HttpResponse('<h1>This page is not accessible</h2>')


def register_user(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			instance = form.save()
			instance.refresh_from_db()

			profile_pic = request.POST.get('profile_pic')
			username = form.cleaned_data.get('username')
			registered_user = User.objects.get(username=username)

			if profile_pic == '':
				UserProfile.objects.create(user=registered_user)
			else:
				UserProfile.objects.create(user=registered_user,profile_pic=profile_pic)
			return redirect('accounts:home')
	else:
		form = UserRegisterForm()
	return render(request, 'accounts/register_form.html', {'form': form})


@login_required(login_url='accounts:login')
def profile(request):
	pass