from django.urls import path
from . import views
from . views import BlogView, ProductView, PostDetailsView, CreatePostView, CreateProductView, UpdatePostView, \
                    UpdateProductView, DeletePost, DeleteProduct

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('products/', ProductView.as_view(), name="products"),
    path('products/create_product', CreateProductView.as_view(), name="product_post"),
    path('products/update_product/<int:pk>/', UpdateProductView.as_view(), name="update_product"),
    path('products/delete_product/<int:pk>/', DeleteProduct.as_view(), name="delete_product"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('blog/create_post', CreatePostView.as_view(), name="blog_post"),
    path('blog/update_post/<int:pk>/', UpdatePostView.as_view(), name="update_post"),
    path('blog/delete_post/<int:pk>/', DeletePost.as_view(), name="delete_post"),
    path('blog/<int:pk>', PostDetailsView.as_view(), name="blog_detail"),
    path('contact/', views.contact, name="contact"),
]

