from django.urls import path
from . import views
from . views import BlogView, PostDetailsView

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('blog/<int:pk>', PostDetailsView.as_view(), name="blog_detail"),
    path('contact/', views.contact, name="contact"),
]

