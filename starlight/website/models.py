from django.db import models

# Create your models here.
class Category(models.Model):
	cat_name = models.CharField(max_length=50)
	cat_photo = models.FileField()

	class Meta:
		verbose_name_plural = "Categories"
		
	def __str__ (self):
		return self.cat_name

class Photo(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	photo_name = models.CharField(max_length=100)
	photo_preview = models.FileField()
	photo_img = models.FileField()

	def __str__ (self):
		return self.photo_name 
		