from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

	title = models.CharField("Название поста", max_length=100, unique=True, db_index=True)
	body = models.TextField("Тело поста", db_index=True, blank=True)
	date_pub = models.DateField(auto_now_add=True, blank=True, null=True)
	picture = models.ImageField(upload_to="pictures/", null=True, blank=True, default='default/default.jpg')
	files = models.FileField(upload_to="files/", default="")
	views = models.IntegerField(default = 0)

	comments = models.ManyToManyField("Comment", blank=True, related_name="posts")

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date_pub']

class Comment(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

	title = models.CharField("Название комментария", max_length=100)
	desc = models.TextField("Описание комментария")
	likes = models.IntegerField(default = 0)

	date_pub = models.DateField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date_pub']
