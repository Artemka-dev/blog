from django.shortcuts import render, redirect, reverse

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

from django.contrib import auth
from .forms import RegistrationForm

from django.template.context_processors import csrf

# Create your views here.
class CreateAccount(View):
	def get(self, request):
		if request.user.is_authenticated:
			return redirect('/')

		form = RegistrationForm()
		return render(request, 'authsys/registration.html', context={'form': form})

	def post(self, request):
		bound_form = RegistrationForm(request.POST)
		if bound_form.is_valid():
			bound_form.save()
			return redirect("login_page")
		else:
			return render(request, 'authsys/registration.html', context={"form": bound_form})


class LoginSite(View):
	def get(self, request):
		active = "login"

		if request.user.is_authenticated:
			return redirect("/")

		return render(request, 'authsys/login.html', context={"active": active})

	def post(self, request):
		args = {}

		args.update(csrf(request))
		username = request.POST.get("username", "")
		password = request.POST.get("passw", "")

		user = auth.authenticate(username = username, password = password)
		if user is not None:
			auth.login(request, user)
			return redirect("home_page")
		else:
			args['errors'] = "Пользователь не найден"
			return render(request, "authsys/login.html", args)

def logout(request):
	auth.logout(request)
	return redirect("/")