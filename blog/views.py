from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class HomePage(TemplateView):
	template_name = "blog/home.html"