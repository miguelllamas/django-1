from django.shortcuts import render

from .models import Post

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django import forms
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user) # Redirect to a success page. ...
		else: # Return an 'invalid login' error message.
			return render(request, 'blog/home')
			
	return render(request, 'blog/index.html') # request index.html in templates folder
	
def signup(request):
	if request.method == 'POST': # HTTP method 'POST': if user submits a form
		# form = UserCreationForm(request.POST)
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password) #authenticate by checking for matching users
			login(request, user) #login
			return redirect('index')
	else:
		# form = UserCreationForm()
		form = SignUpForm()
		
	return render(request, 'blog/signup.html',{'form':form})
	
def home(request):
	return render(request, 'blog/home.html')