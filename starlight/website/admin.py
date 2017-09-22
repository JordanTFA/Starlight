from django.contrib import admin
from .models import Category, Photo
from django.core.files.base import ContentFile

# This all needs sorted so that we can rotate images
# Would be ideal if I just have one rotate function
# instead of 3 (right, left and 180)

class CategoryDetails(admin.ModelAdmin):
    list_display = ('cat_name','pk')
    search_fields = ('cat_name', 'pk')

class PhotoDetails(admin.ModelAdmin):
	list_display = ('photo_name', 'category', 'photo_img', 'photo_is_favourite')
	search_fields = ('photo_name', 'photo_img', 'category__cat_name')
	ordering = ['category__cat_name']

class rotateLeft(admin.ModelAdmin):
	pass
	
    #list_diplay = ('title', 'desc')

    #original_photo = StringIO.StringIO(Photo.file.read())
    #rotated_photo = StringIO.StringIO()

    #image = Image.open(original_photo)
    #image = image.rotate(-90)
    #image.save(rotated_photo, 'PNG')

    #Photo.file.save(image.file.path, ContentFile(rotated_photo.getvalue()))
    #Photo.save()


# Register your models here.
admin.site.register(Category, CategoryDetails)
admin.site.register(Photo, PhotoDetails)
#admin.site.register(rotateLeft)

