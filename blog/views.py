from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404


from .models import Post
from .forms import PostForm


class PostList(ListView):
    model = Post


@require_http_methods(['HEAD', 'GET'])
def post_detail(request, year, month, slug):
    post = get_object_or_404(
        Post,
        pub_date__year=year,
        pub_date__month=month,
        slug=slug)
    return render(
        request,
        'blog/post_detail.html',
        {'post': post})


class PostCreate(CreateView):
    template_name = 'blog/post_form.html'
    form_class = PostForm


class PostUpdate(UpdateView):
    template_name = 'blog/post_update_form.html'
    form_class = PostForm
    model = Post
        
    
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
