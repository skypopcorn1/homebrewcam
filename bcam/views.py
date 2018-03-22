from django.shortcuts import render

def posts_home(request):
	return render(request, 'index.html')
