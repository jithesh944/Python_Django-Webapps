from django.shortcuts import render,redirect
from django.contrib import messages
from .models import ContactUs

# Create your views here.

def contact_us(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company = request.POST['company']
        subject = request.POST['subject']
        explanation = request.POST['message']

        contact_data = ContactUs(full_name=full_name, phone=phone, email=email,company= company,subject=subject,message = explanation)
        contact_data.save()
        messages.success(request, "Thank you for contacting us.")
        return redirect('contact')