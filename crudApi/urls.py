from django.urls import path
from . import views


urlpatterns = [
    path('create-blog', views.CreateBlogAPI.as_view()),
    path('list-blogs', views.ListBlogsAPI.as_view()),
    path('blogs/<int:pk>', views.DetailBlogAPI.as_view()),
    path('update-blog/<int:pk>', views.UpdateBlogAPI.as_view()),
    path('delete-blog/<int:pk>', views.DeleteBlogAPI.as_view()),
    path('search-blog', views.BlogSearchAPI.as_view()),
]

