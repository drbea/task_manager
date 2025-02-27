from django.shortcuts import render, get_object_or_404, redirect
from . models import Task
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

from .forms import TaskForm 

User = get_user_model()

def index(request):
	tasks = Task.objects.all()
	context = {
		"tasks": tasks
	}
	return render(request, "task/index.html", context)

@login_required
def delete_task(request, task_id):
    try:
        task = get_object_or_404(Task, pk=task_id)

        if request.method == 'POST':
            task.delete()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

@login_required
def task_by_user(request, user_id):
	user = get_object_or_404(User, pk = user_id)
	tasks = Task.objects.filter(author = user)
	context = {
		"tasks": tasks
	}
	return render(request, "task/task_by_user.html", context)


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) # Créer une instance de Task sans la sauvegarder
            task.author = request.user # Associer l'utilisateur connecté à la tâche
            task.save() # Sauvegarder la tâche
            return redirect(reverse('task:task_by_user', kwargs={'user_id': request.user.id})) 
            # return redirect('task:task_by_user')  # Rediriger vers la liste des tâches de l'utilisateur
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html', {'form': form})


# def edit_task(request, task_id):
#     task = get_object_or_404(Task, pk=task_id)

#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'status': 'success', 'task': {'title': task.title, 'content': task.content, 'status': task.status}})
#         else:
#             return JsonResponse({'status': 'error', 'errors': form.errors})
#     else:
#         form = TaskForm(instance=task)
#         return render(request, 'task/edit_task_modal.html', {'form': form, 'task': task}) # Pour le modal



@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, author=request.user)  # Vérifier l'auteur

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status')

        if title and status: # Vérifier que les champs obligatoires sont présents
            task.title = title
            task.content = content
            task.status = status
            task.save()
            return JsonResponse({'status': 'success', 'task': {'title': task.title, 'content': task.content, 'status': task.status}})
        else:
            return JsonResponse({'status': 'error', 'message': 'Titre et statut sont obligatoires.'}, status=400)

    else:
        context = {'task': task}
        return render(request, 'task/edit_task.html', context)