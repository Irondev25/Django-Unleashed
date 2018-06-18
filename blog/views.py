from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import View
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404


from .models import Post
from .forms import PostForm

# def post_list(request):
#     return render(request, 'blog/post_list.html', {'post_list':Post.objects.all()})

class PostList(View):
    template_name = 'blog/post_list.html'
    def get(self, request):
        return render(request, self.template_name, {'post_list': Post.objects.all()})


@require_http_methods(['GET', 'HEAD'])
def post_detail(request, year, month, slug):
    post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
    return render(
        request,
        'blog/post_detail.html',
        {'post':post}
    )


class PostCreate(View):
    template_name = 'blog/post_form.html'
    form_class = PostForm

    def get(self, request):
        unbound_form = PostForm()
        return render(request, self.template_name, {'form':unbound_form})
    
    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            return render(request, self.template_name, {'form':bound_form})


class PostUpdate(View):
    template_name = 'blog/post_update_form.html'
    form_class = PostForm
    model = Post

    def get(self, request, year, month, slug):
        post=get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
        unbound_form = PostForm(instance=post)
        context={
            'form': unbound_form,
            'post': post
        }
        return render(request, self.template_name, context)
    
    def post(self, request, year, month, slug):
        post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
        bound_form = PostForm(request.POST, instance=post)
        context = {
            'form':bound_form,
            'post':post
        }
        if bound_form.is_valid():
            updated_post = bound_form.save()
            return redirect(updated_post)
        else:
            return render(request, self.template_name, context)
        
    
class PostDelete(View):
    template_name = 'blog/post_confirm_delete.html'
    model = Post

    def get(self, request, year, month, slug):
        post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
        return render(request, self.template_name, {'post':post})
    
    def post(self, request, year, month, slug):
        post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
        post.delete()
        return('blog:post_list')
