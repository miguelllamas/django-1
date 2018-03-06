from django.shortcuts import render

from .models import Post
from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

from django import forms
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm

from .forms import PostForm

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
			return redirect('post_list')
	else:
		# form = UserCreationForm()
		form = SignUpForm()
		
	return render(request, 'registration/signup.html',{'form':form})
	
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts}) #request = the user request itself, param2 = template file, param3 = data needed by template
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
	
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.description = "Lorem ipsum"
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
	
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk) # pass Post model, pass unique pk value from urls.py
	if request.method == "POST": # user saves edits
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else: # user opens the post to edit
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})