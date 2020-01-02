from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from .models import Post, Comment
from .forms import PostForm, CommentForm

import os

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
		form = CommentForm()

		post = get_object_or_404(Post, id=id)
		comments = post.comments.all()
		post.views += 1
		post.save()
		return render(request, "blog/detail_post.html", context={"comments": comments, "post": post, "form": form})

	def post(self, request, id):
		bound_form = CommentForm(request.POST)
		post = get_object_or_404(Post, id=id)
		comments = post.comments.all()

		if bound_form.is_valid():
			new_comment = bound_form.save()
			post.comments.add(new_comment)

			return redirect("detail_page", id=post.id)

		else:
			error = "Произошла ошибка при создании комментария"
			return render(request, "blog/detail_post.html", context={"comments": comments, "post": post, "error": error, "form": bound_form})

class CreatePost(View):
	
	def get(self, request):
		form = PostForm()

		return render(request, "blog/create_post.html", context={"form": form})

	def post(self, request):
		bound_form = PostForm(request.POST, request.FILES)

		if bound_form.is_valid():
			new_post = bound_form.save()
			return redirect("home_page")

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

def like(request, id_comment, id_post):
	comment = get_object_or_404(Comment, id=id_comment)
	post = get_object_or_404(Post, id=id_post)

	comment.likes += 1
	comment.save()
	return redirect("detail_page", id=id_post)

