from django.shortcuts import render, get_object_or_404
from . models import Task
from django.http import JsonResponse
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

def index(request):
	tasks = Task.objects.all()
	context = {
		"tasks": tasks
	}
	return render(request, "task/index.html", context)

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

def task_by_user(request, user_id):
	user = get_object_or_404(User, pk = user_id)
	tasks = Task.objects.filter(author = user)
	context = {
		"tasks": tasks
	}
	return render(request, "task/task_by_user.html", context)
