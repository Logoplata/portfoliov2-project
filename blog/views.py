from django.shortcuts import render

def allblog(request):
	return render(request, 'blog/allblog.html')
