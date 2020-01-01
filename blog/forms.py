from django import forms
from .models import Post
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