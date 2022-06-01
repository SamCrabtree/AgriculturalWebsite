from audioop import reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, 'index.html', {}) 

def about(request):
    return render(request, 'about.html', {}) 

def goods(request):
    return render (request, 'products.html', {})

class BlogView(ListView):
    model = Post
    template_name = 'blog_list.html'
    ordering = ['post_date']

class PostDetailsView(DetailView):
    model = Post
    template_name = 'blog_post.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')


    


def contact(request):
   if request.method == "POST":
        message_first_name = request.POST['message-first-name']
        message_last_name = request.POST['message-last-name']
        message_company = request.POST['message-company']
        message_email = request.POST['message-email']
        email = 'INSERT EMAIL HERE'
        message_phone = request.POST['message-phone']
        message = request.POST['message']

        send_mail(
            'Service Inquiry: ' + message_first_name + " " + message_last_name,  #SUBJECT
            'Customer Name: ' + message_first_name + " " + message_last_name + "\nCompany: " + message_company + "\nEmail: " + message_email  + '\nPhone: ' + message_phone + '\n \nMessage: \n' + message, #MESSAGE
            email, #FROM EMAILS
            ['INSERT EMAIL HERE'], #TO EMAIL
            fail_silently=False,
        )

        return render(request, 'contact.html', {'message_first_name': message_first_name})
   else:
        return render(request, 'contact.html', {})