from django.shortcuts import render, redirect

def redirect_root(request):
    return redirect('blog:post_list')