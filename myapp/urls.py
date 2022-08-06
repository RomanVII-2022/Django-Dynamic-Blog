"""myproject URL Configuration

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
from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, EditPostView, DeletePostView, AboutView, MailMessageView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('postdetail/<int:pk>', PostDetailView.as_view(), name='postdetail'),
    path('addblog', AddPostView.as_view(), name='addpost'),
    path('editpost/edit/<int:pk>', EditPostView.as_view(), name='editpost'),
    path('deletepost/<int:pk>', DeletePostView.as_view(), name='deletepost'),
    path('aboutus', AboutView, name='about'),
    path('sendmail', MailMessageView.as_view(), name='sendmail'),
    path('getintouch', ContactView.as_view(), name='contact'),
]
