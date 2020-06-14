from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path("", views.homepage, name = "homepage"),
	path("registration", views.registration, name="registration"),
	path("login", views.login_request, name = "login"),
	path("logout", views.logout_request, name = "logout"),
	path("createMatch", views.create_match, name = "createMatch"),
]