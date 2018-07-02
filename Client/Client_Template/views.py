from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import render_to_response
# Create your views here.

def home(request):
	return render(request,'startbootstrap-grayscale/index.html')

def register(request):
	return render(request, 'dist/register.html')

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

def teacher_dashboard(request):
	return render(request, 'dist/teacher_dashboard.html')

def teacher_projects_list(request):
	return render(request, 'dist/teacher_projects_list.html')

def student_projects_list(request):
	return render(request, 'dist/student_projects_list.html')

def show_graph(request):
	return render(request, 'dist/graph_page.html')

def list_students(request):
	return render(request, 'dist/students_list.html')

def mock(request):
	return render(request, 'dist/mock.html')

def student_dashboard(request):
	return render(request, 'dist/student_dashboard.html')

def student_modules_list(request):
	return render(request, 'dist/student_modules_list.html')

def submit_code(request):
	return render(request, 'dist/submit_code.html')