from django.shortcuts import render

from .models import Project

def allprojects(request):
	projects = Project.objects
	return render(request, 'projects/projects.html', {'projects':projects})