from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
	return render(request, 'website/index.html', {'context': "context"})

def gallery(request):
	return render(request, 'website/gallery.html', {'context': "context"})