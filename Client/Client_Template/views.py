from django.shortcuts import render, redirect

# Create your views here.

def home(request):
	return render(request,'dist/index.html')

def register(request):
	return render(request,'dist/register.html')

def login(request):
	return render(request, 'dist/login.html')


def forgot_password(request):
	return render(request, 'dist/forgot-password.html')

def form_elements(request):
	return render(request, 'dist/form-elements.html')

def create_project(request):
	return render(request, 'dist/create_project.html')

def create_modules(request):
	return render(request, 'dist/create_modules.html')

def dashboard(request):
	return render(request, 'dist/profile.html')

