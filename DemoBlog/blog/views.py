from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
import requests
from .models import Post
from .forms import CustomUserCreationForm, PostForm
from django.contrib.auth.decorators import login_required

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
@login_required
def joke_post_view(request):
    if request.method == "POST":
        # standard post submit
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)    
            post.author = request.user        
            post.save()
            return redirect("post_list")      
    else:
        # generate random joke only when GET
        joke_data = requests.get("https://official-joke-api.appspot.com/random_joke").json()
        initial_data = {
            "title": joke_data["setup"],
            "content": joke_data["punchline"]
        }
        form = PostForm(initial=initial_data)

    return render(request, "post_form.html", {"form": form})

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy('post_list')


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('post_list')
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})