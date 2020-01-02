from django.urls import path
from .views import *


urlpatterns = [
	path("", HomePage.as_view(), name="home_page"),
	path("detail/<str:id>/", DetailPage.as_view(), name="detail_page"),
	path("create_post/", CreatePost.as_view(), name="create_page"),
	path("change_post/<str:id>/", ChangePost.as_view(), name="change_page"),
	path("delete_post/<str:id>/", delete_post, name="delete_post"),
	path("like/<str:id_comment>/<str:id_post>", like, name="like_page")
]