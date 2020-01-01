from django.urls import path
from .views import *


urlpatterns = [
	path("", HomePage.as_view(), name="home_page"),
	path("detail/<str:id>", DetailPage.as_view(), name="detail_page")
]