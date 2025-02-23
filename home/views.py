from django.shortcuts import render

# Create your views here.

def index(request):

	return render(request, "home/index.html", context={})

def about(request):

	return render(request, "home/about.html", context={})

def profile(request):

	return render(request, "home/profile.html", context={})