"""mylib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from lib import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',views.Admin_book_Control_api.as_view()),
    path('book/<int:pk>/',views.Admin_book_Control_api.as_view()),
    path('student/',views.Student_Record_Control_api.as_view()),
    path('student/<int:pk>/',views.Student_Record_Control_api.as_view()),
    path('issue/',views.IssueBook.as_view()),
    path('submit-issue-book/', views.SubmitIssueBook.as_view()),
    path('user-login/',views.User_Login.as_view()),
    path('change-password/',views.User_change_password.as_view()),
    path('register-user/',views.Register_User.as_view()),
    path('update-user/',views.User_update.as_view()),
    path('testing/',views.testing.as_view()),
]

