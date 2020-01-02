from django.shortcuts import render, redirect, reverse

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from django.contrib import auth
from .forms import RegistrationForm, ChangeForm

from django.template.context_processors import csrf
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash

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

class ChangeUserInfo(LoginRequiredMixin, View):

	active = "change"

	def get(self, request):
		form = ChangeForm(instance=request.user)
		return render(request, "authsys/change_form.html", context={"form": form, "active": self.active})

	def post(self, request):
		bound_form = ChangeForm(request.POST, instance=request.user)

		if bound_form.is_valid():
			change = bound_form.save()
			return redirect("home_page")
		else:
			error = "Невозможно изменить пользователя!"
			return render(request, "authsys/change_form.html", context={"form": bound_form, "error": error, "active": self.active})

class ChangePassword(LoginRequiredMixin, View):

	def get(self, request):

		form = PasswordChangeForm(request.user)
		return render(request, "authsys/change_password.html", context={"form": form})

	def post(self, request):
		bound_form = PasswordChangeForm(request.user, request.POST)

		if bound_form.is_valid():
			user = bound_form.save()
			update_session_auth_hash(request, user)
			return redirect("logout")
		else:
			error = "Произошла ошибка. Невозможно изменить пароль!"
			return redirect(request, "authsys/change_password.html", context={"form": bound_form})


@login_required
def logout(request):
	auth.logout(request)
	return redirect("/")