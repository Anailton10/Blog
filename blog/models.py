from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, blank=True, null=True
    )

    def __str__(self):
        return str(self.author)
