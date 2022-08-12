from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


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
				return redirect('todo:homegroup_list')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login_form.html', {'form': form})



def logout_user(request):
	if request.method == 'POST':
		logout(request)
		return redirect('accounts:login')
	else:
		return render(request, 'todo/forbidden.html')


def register_user(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('accounts:login')
	else:
		form = UserRegisterForm()
	return render(request, 'accounts/register_form.html', {'form': form,})


@login_required(login_url='accounts:login')
def profile(request):
	if request.method == 'POST':
		form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
		if form.is_valid():
			form.save()
			return redirect('todo:homegroup_list')
	else:
		form = ProfileUpdateForm(instance=request.user.userprofile)
	return render(request, 'accounts/profile_update.html', {'form': form})


@login_required(login_url='accounts:login')
def profile_update(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(request, username=username, password=password)
			if user:
				login(request, user)
				return redirect('todo:homegroup_list')
	else:
		form = UserRegisterForm(instance=request.user)
	return render(request, 'accounts/profile_update.html', {'form': form})


