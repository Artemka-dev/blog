from django.db import models

# Create your models here.
class Post(models.Model):

	title = models.CharField(max_length=100, db_index=True)
	body = models.TextField(db_index=True, blank=True)
	date_pub = models.DateField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.title