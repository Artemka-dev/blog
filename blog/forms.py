from django import forms
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ["files", 'picture', 'title', "body"]

		widgets = {
			"title": forms.TextInput(attrs={"placeholder": "Название поста"}),
			"body": forms.Textarea(attrs={"placeholder": "Описание"})
		}

		labels = {
			"title": _("Название"),
			"body": _("Описание*")
		}

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ['title', "desc"]

		widgets = {
			"title": forms.TextInput(attrs={"placeholder": "Навазние"}),
			"desc": forms.Textarea(attrs={"placeholder": "Тело комментария"})
		}

		labels = {
			"title": _("Название комментария"),
			"body": _("Описание комментария;")
		}

