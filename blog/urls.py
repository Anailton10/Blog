from django.urls import path

from blog import views

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("create/", views.create_post, name="create"),
    path('category/', views.category, name="category"),
]
