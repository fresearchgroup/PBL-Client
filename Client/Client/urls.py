"""Client URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Client_Template import views as Templ_Views
urlpatterns = [
    #path('profile_page/', Templ_Views.profile_page, name='profile_page'),
    path('submit_code/', Templ_Views.submit_code, name='submit_code'),
    path('student_modules/', Templ_Views.student_modules_list, name='student_modules_list'),
    path('student_dashboard/', Templ_Views.student_dashboard, name='student_dashboard'),
    path('mock/', Templ_Views.mock, name='mock'),
    path('students/', Templ_Views.list_students, name='list_students'),
    path('graph/', Templ_Views.show_graph, name='show_graph'),
    path('student_projects/', Templ_Views.student_projects_list, name='student_projects_list'),
    path('teacher_projects/', Templ_Views.teacher_projects_list, name='teacher_projects_list'),
    path('teacher_dashboard/', Templ_Views.teacher_dashboard, name='teacher_dashboard'),
    path('create_modules/', Templ_Views.create_modules, name='add_modules'),
    path('create_project/', Templ_Views.create_project, name='create_project'),
    path('form_elements/', Templ_Views.form_elements, name='form_elements'),
    path('login/forgot_password/', Templ_Views.forgot_password, name='login/forgot_password'),
    path('login/',Templ_Views.login, name='login'),
	path('register/', Templ_Views.register),
	path('', Templ_Views.home),
    path('admin/', admin.site.urls),
]
