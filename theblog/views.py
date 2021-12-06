from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy

class HomeView(ListView):
        model = Post
        template_name = 'home.html'
        ordering = ['-post_date']
        #ordering = ['-id']

class ArticleDetailView(DetailView):
        model = Post
        template_name = 'articledetail.html'

class AddPostView(CreateView):
        model = Post
        form_class = PostForm
        template_name = 'add_post.html'
        #fields = '__all__'

class UpdatePostView(UpdateView):
        model = Post
        form_class = EditForm
        template_name = 'update_post.html'
        #fields = '__all__'
        #fields = ['title', 'title_tag', 'body']

class AddCommentView(CreateView):
        model = Comment
        form_class = CommentForm
        template_name = 'add_comment.html'

        def form_valid(self, form):
                form.instance.post_id =self.kwargs['pk']
                return super().form_valid(form)

        success_url = reverse_lazy('home')
        #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
        model = Post
        template_name = 'delete_post.html'
        success_url = reverse_lazy('home')