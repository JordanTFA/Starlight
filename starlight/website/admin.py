from django.contrib import admin
from .models import Category, Photo, Top_Photo
from django.core.files.base import ContentFile

# This all needs sorted so that we can rotate images
# Would be ideal if I just have one rotate function
# instead of 3 (right, left and 180)
def rotateLeft(request,id):
    myModel = myModel.objects.get(pk=id)

    original_photo = StringIO.StringIO(myModel.file.read())
    rotated_photo = StringIO.StringIO()

    image = Image.open(original_photo)
    image = image.rotate(-90)
    image.save(rotated_photo, 'JPEG')

    myModel.file.save(image.file.path, ContentFile(rotated_photo.getvalue()))
    myModel.save()


# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Top_Photo)

