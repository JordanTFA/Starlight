from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category

def index(request):
	return render(request, 'website/index.html', {'context': "context"})

def gallery(request):

	all_categories = Category.objects.order_by('cat_name')
	context = {'all_categories' : all_categories}
	return render(request, 'website/gallery.html', context)