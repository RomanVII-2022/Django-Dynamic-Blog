from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post
from .forms import AddPostForm, EditPostForm
from django.urls import reverse_lazy

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'postdetail.html'


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'addblog.html'


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'editpost.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')


def AboutView(request):
    return render(request, 'about.html')


