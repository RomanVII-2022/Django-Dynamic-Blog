from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post, MailMessage, Subscriber, Contact
from .forms import AddPostForm, EditPostForm, MailMessageForm, ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'


    def post(self, request, **kwargs):
        if request.method == "POST":
            email = request.POST['semail1']
            save_data = Subscriber(email=email)
            save_data.save()
            messages.success(request, 'Subscription was successful')
            return redirect('home')



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
    if request.method == "POST":
            email = request.POST['semail1']
            save_data = Subscriber(email=email)
            save_data.save()
            messages.success(request, 'Subscription was successful')
            return redirect('about')

    return render(request, 'about.html')


class MailMessageView(SuccessMessageMixin, CreateView):
    model = MailMessage
    form_class = MailMessageForm
    template_name = 'sendmail.html'
    success_message = "Newsletters have been sent successfully"

    

class ContactView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_message = "Your message has been sent successfully"


    


