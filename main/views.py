from django.shortcuts import render, redirect #To render templates, to send users to other page
from django.http import HttpResponse #To use Simple HTTP Response
from django.contrib.auth.models import User # For User
from .models import Match, UserProfile #Model which stores our Matches data
from django.contrib.auth.forms import AuthenticationForm #For Forms
from django.contrib.auth import login, logout, authenticate #For Login, Logout and authentication
from django.contrib import messages #For different MESSAGES, ie error messages..	
from .forms import NewUserForm, NewUserProfileForm, NewMatchForm #Add different FORMS
from .filters import MatchFilter #Adding search filters
# Create your views here.

"""---------------HOMEPAGE---------------"""
def homepage(request):
	if(request.method == "POST"):
		matches  = Match.objects.all()
		myFilter  = MatchFilter(request.POST, queryset = matches)
		FilteredMatches = myFilter.qs
		if(len(FilteredMatches) == 0):
			messages.info(request, "Sorry No Matches Found :(")
			messages.info(request,"Try shortening the search query!	")
		return render(request = request, template_name = "main/index.html", context  = {"FilteredMatches" : FilteredMatches, "myFilter" : myFilter})
	else:
		myFilter = MatchFilter()
		return render(request = request, template_name = "main/index.html", context  = {"myFilter" : myFilter})


"""---------------Registration---------------"""
def registration(request):
	if(request.method == "POST"):
		form = NewUserForm(request.POST)
		prof_form = NewUserProfileForm(request.POST)
		if (form.is_valid() and prof_form.is_valid()):
			user = form.save()
			UserProfile.objects.create(user=user, age= prof_form.cleaned_data.get('age'), city = prof_form.cleaned_data.get('city'))
			username= form.cleaned_data.get('username')
			messages.success(request,f"New Account Created!: {username}")
			login(request,user)
			messages.info(request,f"You are now logged in as: {username}")
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, form.error_messages[msg])

	form = NewUserForm
	prof_form = NewUserProfileForm
	return render(request,"main/registration.html",context = {"form":form,"prof_form":prof_form})

"""---------------LogOut---------------"""
def logout_request(request):
	logout(request)
	messages.info(request, "Logged Out Sucessfully!")
	return redirect("main:homepage")

"""---------------Log In---------------"""
def login_request(request):
	if (request.method == "POST"):
		form = AuthenticationForm(request, data = request.POST)
		if (form.is_valid()):
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username= username, password = password)

			if (user is not None):
				login(request,user)
				messages.info(request, f"You have logged in successfuly as: {username}")
				return redirect("main:homepage")

			else:
				messages.error(request, "Invalid Username or password!")

		else:
			messages.error(request, "Invalid username or password!")
	form = AuthenticationForm()
	return render(request, "main/login.html", {"form":form})

"""---------------Log In---------------"""
def create_match(request):
	if(request.method == "POST"):
		form = NewMatchForm(request.POST)
		if(form.is_valid()):
			location = form.cleaned_data.get('location')
			sport	 = form.cleaned_data.get('sport')
			maxPlayers = form.cleaned_data.get('maxPlayers')
			dateMatch = form.cleaned_data.get('date')
			timeMatch = form.cleaned_data.get('time')

			""" create match object """
			match = Match.objects.create(location = location,sport = sport, maxPlayers = maxPlayers, date= dateMatch, time = timeMatch)
			messages.success(request, "Match Created successfuly")
			messages.info(request, f"Match ID :{match.id} " )
			return redirect("main:homepage")


	form = NewMatchForm
	return render(request, "main/createMatch.html",{"form": form})