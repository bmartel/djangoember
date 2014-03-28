from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response
from .models import *


def index(request):
    """Post listing."""
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 2)

    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("blog/list.html", dict(posts=posts, user=request.user))