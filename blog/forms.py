from django import forms

from blog.models import BlogPost


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = "__all__"
