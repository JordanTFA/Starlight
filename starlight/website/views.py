from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Photo

def indexView(request):
	return render(request, 'website/index.html', {'context': "context"})

def galleryView(request):

	all_categories = Category.objects.order_by('cat_name')
	context = {'all_categories' : all_categories}
	return render(request, 'website/gallery.html', context)

def categoryView(request, cat_name_from_url):

	c = Category.objects.get(pk=1)

	the_photos = c.photo_set.all()
	return render(request, 'website/photos.html', {'the_photos': the_photos})