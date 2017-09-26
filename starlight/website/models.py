from django.db import models

# Category for photos (E.g. Christmas, Halloween)
class Category(models.Model):
	cat_name = models.CharField(max_length=50)
	cat_photo = models.ImageField()

	class Meta:
		verbose_name_plural = "Categories"
		
	def __str__ (self):
		return self.cat_name

	def __unicode__(self):
		return self.cat_name

# Actual photo
class Photo(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	photo_name = models.CharField(max_length=100, blank=True, unique=False)
	photo_is_favourite = models.BooleanField(default=False)
	photo_img = models.ImageField()

	def __str__ (self):
		return self.photo_name 