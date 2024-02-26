from django import forms

from blog.models import BlogPost


class CreateBlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = "__all__"
