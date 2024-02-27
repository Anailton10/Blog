from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CreatePostForm
from .models import BlogPost, Category, Language


class Home(ListView):
    model = BlogPost
    template_name = "blog.html"
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        posts = BlogPost.objects.all().order_by("-id")

        category_id = self.request.GET.get("category_id")
        language_id = self.request.GET.get("language_id")

        if category_id:
            posts = posts.filter(category__id=category_id)

        if language_id:
            posts = posts.filter(language__id=language_id)

        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()
        languages = Language.objects.all()

        posts = context["posts"]  # context_object_name

        paginator = Paginator(posts, self.paginate_by)

        page_num = self.request.GET.get("page")

        pages = paginator.get_page(page_num)

        # Adiciona os objetos ao contexto
        context["categories"] = categories
        context["languages"] = languages
        context["posts"] = pages

        return context


class Detail(DetailView):
    model = BlogPost
    template_name = "detail.html"
    context_object_name = "post"


@method_decorator(login_required(login_url="login"), name="dispatch")
class CreatePost(CreateView):
    model = BlogPost
    form_class = CreatePostForm
    template_name = "create_post.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_form"] = context["form"]  # sobrescrevendo context padrão
        return context


@method_decorator(login_required(login_url="login"), name="dispatch")
class UpdatePost(UpdateView):
    model = BlogPost
    form_class = CreatePostForm
    template_name = "update_post.html"

    def get_success_url(self):
        return reverse_lazy("detail", kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url="login"), name="dispatch")
class DeletePost(DeleteView):
    model = BlogPost
    template_name = "delete_post.html"
    success_url = '/home/'


