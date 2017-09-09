from django.contrib import admin
from .models import Category, Photo, Top_Photo

# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Top_Photo)

