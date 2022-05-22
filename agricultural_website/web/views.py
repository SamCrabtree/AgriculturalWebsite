from django.shortcuts import render

from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'index.html', {}) 

def about(request):
    return render(request, 'about.html', {}) 

def blog(request):
    return render(request, 'blog.html', {})

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