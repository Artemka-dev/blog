from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from .models import Post
from .forms import PostForm

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


class CreatePost(View):
	
	def get(self, request):
		form = PostForm()

		return render(request, "blog/create_post.html", context={"form": form})

	def post(self, request):
		bound_form = PostForm(request.POST, request.FILES)

		if bound_form.is_valid():
			new_post = bound_form.save()
			return redirect("home_page")
		else:
			error = "Невозможно создать пост"
			return render(request, "blog/create_post.html", context={"error": error, "form": bound_form})

class ChangePost(View):

	def get(self, request, id):
		post = Post.objects.get(id=id)
	
		form = PostForm(instance=post)
		return render(request, "blog/change_post.html", context={"form": form, "post": post})

	def post(self, request, id):
		post = Post.objects.get(id=id)
		bound_form = PostForm(request.POST, request.FILES, instance=post)

		if bound_form.is_valid():
			update = bound_form.save()
			return redirect("home_page")
		else:
			error = "Невозможно пересоздать пост"
			return render(request, "blog/create_post.html", context={"form": bound_form, "error": error, "post": post})


def delete_post(request, id):
	post = Post.objects.get(id=id)
	post.delete()
	return redirect("home_page")

