from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Portfolio
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def home(request):
    return render(request,'mainapp/home.html')



def about(request):
    return render(request,'mainapp/about.html')


def projects(request):
    data=Portfolio.objects.all()
    print(data)
    context= {
        "data":data
    }
    return render(request,'mainapp/projects.html',context)


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            Enter_email = form.cleaned_data['Enter_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, Enter_email, [Enter_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "mainapp/contact.html", {'form': form})

    

def successView(request):
    return HttpResponse('Success! Thank you for your message.')