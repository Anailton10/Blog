from django.urls import path

from blog import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"),
    path("create/", views.CreatePost.as_view(), name="create"),
    path("update/<int:pk>/", views.UpdatePost.as_view(), name="updade"),
    path("delete/<int:pk>/", views.DeletePost.as_view(), name="delete"),
]
