from django.shortcuts import render

from .models import Project

def allprojects(request):
	return render(request, 'projects/projects.html')