from django.shortcuts import render, redirect

def redirect_to(request):
	return redirect("home_page")