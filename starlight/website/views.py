from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Category, Photo

# Homepage
def indexView(request):

	# Get all of the favourite photos to be displayed on the homepage
	all_favourite_photos = Photo.objects.filter(photo_is_favourite=True)

	context = {"all_favourite_photos" : all_favourite_photos}
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

	c = get_object_or_404(Category, cat_name=the_cat)
	the_photos = c.photo_set.all()

	context = {'the_photos': the_photos, 'cat_name' : the_cat}
	return render(request, 'website/photos.html', context)