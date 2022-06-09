
from django.shortcuts import render, redirect,get_object_or_404
from django.http  import HttpResponse, Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post, Profile
from django import template
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ImageList(ListView):
    model = Post
    template_name = 'photos/post_list.html'

    def get_queryset(self):
        return Post.objects.all()

def image_list(request):
    posts = models.Post.objects.all()
    return render(request, "photos/post_list.html", {'post':post})

def viewPhoto(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        value = request.POST['value']
        comments = request.POST['comments']
        if value == 'comments':
            comments.save()
    return render(request, 'photos/image.html', {'post':post})

class ProfileList( ListView):
    model = Profile
    template_name = 'photos/profile_list.html'

    def get_queryset(self):
        return Profile.objects.all()