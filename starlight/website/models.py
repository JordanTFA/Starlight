from django.db import models

# Create your models here.
class Category(models.Model):
	cat_name = models.CharField(max_length=50)
	cat_photo = models.IntegerField(default=1) # IMPORTANT: This will be changed to an imageField in the future to represent the category photo

	class Meta:
		verbose_name_plural = "Categories"
		
	def __str__ (self):
		return self.cat_name

class Photo(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	photo_name = models.CharField(max_length=30)

	def __str__ (self):
		return '(' + self.category + ') ' + self.photo_name 
