from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .forms import CreateBlogPostForm
from .models import BlogPost

# TODO: categorias e linguagem ver possibilidades para filtragem


# Create your views here.
def home(request):
    posts = BlogPost.objects.all().order_by("-id")

    paginator = Paginator(posts, 2)
    page_num = request.GET.get("page")
    pages = paginator.get_page(page_num)

    return render(request, "blog.html", {"posts": pages})


def detail(request, pk):
    post = BlogPost.objects.get(id=pk)

    return render(request, "detail.html", {"post": post})


@login_required()
def create_post(request):
    if request.method == "POST":
        post_form = CreateBlogPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect("home")
        else:
            return render(request, "register_post.html", {"post_form": post_form})
    else:
        post_form = CreateBlogPostForm()
        return render(request, "register_post.html", {"post_form": post_form})
