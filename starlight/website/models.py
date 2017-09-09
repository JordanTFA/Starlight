from django.db import models

# Create your models here.
class Category(models.Model):
	cat_name = models.CharField(max_length=50)
	cat_photo = models.ImageField()

	class Meta:
		verbose_name_plural = "Categories"
		
	def __str__ (self):
		return self.cat_name

class Photo(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	photo_name = models.CharField(max_length=100, blank=True, unique=False)
	photo_img = models.ImageField()

	def __str__ (self):
		return self.photo_name 
		
class Top_Photo(models.Model):
	top_photo_name = models.CharField(max_length=100)
	top_photo_img = models.ImageField()

	class Meta:
		verbose_name_plural = "Top Photos"

	def __str__ (self):
		return self.top_photo_name