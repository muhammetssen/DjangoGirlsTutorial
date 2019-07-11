from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request,'blog/post_list.html',{
        'posts':posts


    })

"""def new_post(request):
    return render

    """