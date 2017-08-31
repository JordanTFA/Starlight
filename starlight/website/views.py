from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category

def indexView(request):
	return render(request, 'website/index.html', {'context': "context"})

def galleryView(request):

	all_categories = Category.objects.order_by('cat_name')
	context = {'all_categories' : all_categories}
	return render(request, 'website/gallery.html', context)

def categoryView(request, cat_name):

	all_photos = Category.objects.order_by('cat_name')	# TODO: needs fixed so that it shows all photos in a category
	context = {'all_categories' : all_photos}

	return render(request, 'website/photos.html', context)