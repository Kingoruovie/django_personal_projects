from django.shortcuts import render
from .models import Project


def home(request):
	return render(request, 'project_app/home.html')


def resume(request):
	return render(request, 'project_app/resume.html')


def all_project(request):
	projects = Project.objects.all()
	return render(request, 'project_app/projects.html', {'projects': projects})


def project_detail(request, pk):
	project = Project.objects.get(id=pk)
	return render(request, 'project_app/project_detail.html', {'project': project})