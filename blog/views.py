from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView

from .models import Post

# Create your views here.
class HomePage(TemplateView):
	template_name = "blog/home.html"

	def get_context_data(self, *args, **kwargs):
		context = super(HomePage, self).get_context_data(*args, **kwargs)
		
		posts = Post.objects.all()
		context['active'] = "home"
		context['posts'] = posts
		return context

class DetailPage(View):

	def get(self, request, id):
		post = get_object_or_404(Post, id=id)
		return render(request, "blog/detail_post.html", context={"post": post})