from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Portfolio
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
# import settings


def home(request):
    return render(request,'mainapp/home.html')



def about(request):
    return render(request,'mainapp/about.html')


def projects(request):
    data=Portfolio.objects.all()
    context= {
        "data": data
    }
    return render(request,'mainapp/projects.html',context)


def contact(request):
   
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        try:
            if form.is_valid():
                subject = form.cleaned_data['subject']
                name = form.cleaned_data['name']
                from_mail = form.cleaned_data['from_mail']
                message = form.cleaned_data['message']
            
                try:
                    send_mail(subject, 'Hello ' + name + ',\n'+ from_mail + ',\n' + message, from_mail, ['jyothiprakash097@gmail.com'],fail_silently=True)
                except BadHeaderError:
                    return HttpResponse('In/contactvalid header found.')
                return redirect('success')
        except:
            return HttpResponse("Mail is Not Working Properly")
    return render(request, "mainapp/contact.html", {'form': form})

    

def successView(request):
    return render(request,"mainapp/success.html")

def blog(request):
    return render(request,"mainapp/blog.html")