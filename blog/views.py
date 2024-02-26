from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .forms import CreateBlogPostForm
from .models import BlogPost, Category, Language


def home(request):
    posts = BlogPost.objects.all().order_by("-id")
    category_id = request.GET.get("category_id")
    language_id = request.GET.get("language_id")

    categories = Category.objects.all()
    languages = Language.objects.all()

    if category_id:
        posts = posts.filter(category__id=category_id)

    if language_id:
        posts = posts.filter(language__id=language_id)

    paginator = Paginator(posts, 2)
    page_num = request.GET.get("page")
    pages = paginator.get_page(page_num)

    return render(
        request,
        "blog.html",
        {"posts": pages, "categories": categories, "languages": languages},
    )


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


def category(request):
    categories = Category.objects.all()
    return render(request, "blog.html", {"categories": categories})
