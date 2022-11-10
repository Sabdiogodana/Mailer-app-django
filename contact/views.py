from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .form import CustomerContactForm

# Create your views here.
 
def index(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(email,subject,message)

        return HttpResponse("Email has been sent")
        send_mail(
          full_name, subject,sabdiogodanaj@gmail.com,message
            [email]
        )
                  
    return render(request, 'contact/form.html')




# Create your views here.
