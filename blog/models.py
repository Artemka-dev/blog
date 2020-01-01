from django.db import models

# Create your models here.
class Post(models.Model):

	title = models.CharField(max_length=100, unique=True, db_index=True)
	body = models.TextField(db_index=True, blank=True)
	date_pub = models.DateField(auto_now_add=True, blank=True, null=True)
	picture = models.ImageField(upload_to="pictures/", null=True, blank=True, default='default/default.jpg')

	def __str__(self):
		return self.title