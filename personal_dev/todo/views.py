from django.shortcuts import render, redirect
from .models import Task, TaskGroup
from .forms import TaskGroupForm, TaskForm
from datetime import datetime
from django.contrib.auth.decorators import login_required


# A default value for taskgroup name
today = datetime.now()
name_default = today.strftime('%A, %d. %B %Y %I:%M%p %S')
slug_default = '-'.join(today.strftime('%A %d %B %Y %I %M%p %S').split(' '))


@login_required(login_url='accounts:login')
def homepage(request):
	"""Displays a list of all group of task created."""

	groups = TaskGroup.objects.filter(user=request.user).order_by('-date')
	context = {
		'groups': groups,
	}

	return render(request, 'todo/groups.html', context)


# The CRUD for the group which is basically a way to gather a todo list created
# for in a particluar niche
@login_required(login_url='accounts:login')
def group_create(request):
	if request.method == 'POST':
		form = TaskGroupForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			if request.POST.get('name'):
				instance.slug = '-'.join(request.POST.get('name').split())
			else:
				instance.name = name_default
				instance.slug = slug_default
			instance.save()
			return redirect('todo:homegroup_list')
	else:
		form = TaskGroupForm()
	return render(request, 'todo/group_create.html', {'form': form})

@login_required(login_url='accounts:login')
def group_update(request, pk):
	group = TaskGroup.objects.get(id=pk)
	if request.method == 'POST':
		form = TaskGroupForm(request.POST, instance=group)
		if form.is_valid():
			form.save()
			return redirect('todo:homegroup_list')
	else:
		form = TaskGroupForm(instance=group)
	return render(request, 'todo/group_update.html', {'form': form})
	
@login_required(login_url='accounts:login')
def group_delete(request, pk):
	if request.method == 'POST':
		group = TaskGroup.objects.get(id=pk)
		group.delete()
		return redirect('todo:homegroup_list')
	else:
		return render(request, 'todo/forbidden.html')

@login_required(login_url='accounts:login')
def group_detail(request, pk):
	group = TaskGroup.objects.get(id=pk)
	task_list = group.task_set.all().order_by('priority', 'title')
	context = {
		'task_list': task_list,
		'group': group,
	}

	return render(request, 'todo/group_detail.html', context)



# The CRUD functionality of the task the or items in the todolist
@login_required(login_url='accounts:login')
def task_detail(request, pk):
	task = Task.objects.get(id=pk)
	context = {
		'task': task,
	}

	return render(request, 'todo/task_detail.html', context)

@login_required(login_url='accounts:login')
def task_create(request, pk):
	group = TaskGroup.objects.get(id=pk)
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.group = group
			instance.save()
			return redirect('todo:group_detail', group.id)
	else:
		form = TaskForm()
	return render(request, 'todo/task_create.html', {'form': form,})

@login_required(login_url='accounts:login')
def task_update(request, pk):
	task = Task.objects.get(id=pk)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('todo:group_detail', task.group.id)
	else:
		form = TaskForm(instance=task)
	return render(request, 'todo/task_update.html', {'form': form})

@login_required(login_url='accounts:login')
def task_delete(request, pk):
	if request.method == 'POST':
		task = Task.objects.get(id=pk)
		pk = task.group.id
		task.delete()
		return redirect('todo:group_detail', pk)
	return render(request, 'todo/forbidden.html')

@login_required(login_url='accounts:login')
def task_completeness(request, pk):
	task = Task.objects.get(id=pk)
	group = task.group
	if task.status:
		task.status = False
	else:
		task.status = True
	task.save()
	return redirect('todo:group_detail', group.id)