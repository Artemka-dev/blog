import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, View

from .forms import CommentForm, PostForm
from .models import Comment, Post


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
			new_comment = Comment.objects.create(user=request.user, title=bound_form.cleaned_data['title'], desc=bound_form.cleaned_data['desc'])
			post.comments.add(new_comment)

			return redirect("detail_page", id=post.id)

		else:
			error = "Произошла ошибка при создании комментария"
			return render(request, "blog/detail_post.html", context={"comments": comments, "post": post, "error": error, "form": bound_form})

class CreatePost(LoginRequiredMixin, View):
	
	def get(self, request):
		form = PostForm()

		return render(request, "blog/create_post.html", context={"form": form})

	def post(self, request):
		bound_form = PostForm(request.POST, request.FILES)

		if bound_form.is_valid():
			new_post = Post.objects.create(user=request.user, title=bound_form.cleaned_data["title"], body=bound_form.cleaned_data['body'], files=bound_form.cleaned_data['files'], picture=bound_form.cleaned_data['picture'])
			return redirect("home_page")

		error = "Невозможно создать пост"
		return render(request, "blog/create_post.html", context={"error": error, "form": bound_form})

class ChangePost(LoginRequiredMixin, View):

	def get(self, request, id):
		post = Post.objects.get(id=id)
		if post.user != request.user:
			return redirect("detail_page", id=id)
	
		form = PostForm(instance=post)
		return render(request, "blog/change_post.html", context={"form": form, "post": post})

	def post(self, request, id):
		post = Post.objects.get(id=id)
		bound_form = PostForm(request.POST, request.FILES, instance=post)

		if bound_form.is_valid():
			update = bound_form.save(request.user)
			return redirect("home_page")
		else:
			error = "Невозможно пересоздать пост"
			return render(request, "blog/create_post.html", context={"form": bound_form, "error": error, "post": post})

@login_required
def delete_post(request, id):
	post = Post.objects.get(id=id)
	if post.user != request.user:
		return redirect("detail_page", id=id)

	comments = post.comments.all()
	post.delete()
	comments.delete()
	return redirect("home_page")
