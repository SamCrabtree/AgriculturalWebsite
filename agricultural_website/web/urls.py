from django.urls import path
from . import views
from . views import BlogView, PostDetailsView, CreatePostView, UpdatePostView, DeletePost

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('goods/', views.goods, name="goods"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('blog/create_post', CreatePostView.as_view(), name="blog_post"),
    path('blog/update_post/<int:pk>/', UpdatePostView.as_view(), name="update_post"),
    path('blog/delete_post/<int:pk>/', DeletePost.as_view(), name="delete_post"),
    path('blog/<int:pk>', PostDetailsView.as_view(), name="blog_detail"),
    path('contact/', views.contact, name="contact"),
]

