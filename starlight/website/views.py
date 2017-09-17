from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Photo, Top_Photo

# Homepage
def indexView(request):

	# Get all of the photos to be displayed on the homepage
	all_top_photos = Top_Photo.objects.all()
	context = {"all_top_photos" : all_top_photos}
	return render(request, 'website/index.html', context)

# Gallery
def galleryView(request):

	# Get all the photo categories
	all_categories = Category.objects.order_by('cat_name')
	context = {'all_categories' : all_categories}
	return render(request, 'website/gallery.html', context)

# Photos inside of a category
def categoryView(request, cat_name_from_url):

	# Get all photos in the chosen category
	the_cat = cat_name_from_url
	c = Category.objects.get(cat_name=the_cat)
	the_photos = c.photo_set.all()

	context = {'the_photos': the_photos}
	return render(request, 'website/photos.html', context, the_cat)