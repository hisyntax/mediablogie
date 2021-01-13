from django.db.models import Q
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post

def post_list(request):
    post = Post.objects.all()
    lattest = Post.objects.order_by('-timestamp')[:3]
    content = {
        'post': post,
        'lattest': lattest
    }
    return render (request, 'index.html', content)

    

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    lattest = Post.objects.order_by('-timestamp')[:3]
    content = {
        'post': post,
        'lattest': lattest
    }
    return render (request, 'blog.html', content)


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)

        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)

