from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Post

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=100, required=True, help_text='Your first name.')
	last_name = forms.CharField(max_length=100, required=True, help_text='Your last name.')
	email = forms.EmailField(max_length=254, required=False, help_text='A valid email address (optional).')
	
	model = User
	fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
	
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)		
		self.fields['password1'].help_text = 'Must contain at least 8 characters. Cannot be entirely numeric.'
		
	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		if commit:
			user.save()
			
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content',)