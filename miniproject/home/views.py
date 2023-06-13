from django.shortcuts import render
from django.http import HttpResponse
from.models import Departments,Doctors
from.forms import Bookingform
from django.contrib import messages
from django.shortcuts import render, redirect




# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
     return render(request,'about.html')

def booking(request):
     if request.method == "POST":
          form = Bookingform(request.POST)
          if form.is_valid():
               form.save()
               return render(request,'conformation.html')
     form = Bookingform
     dict_form={
          'form': form
     }
     return render(request,'booking.html',dict_form)

def doctors(request):
     dict_doc={
          'doc':Doctors.objects.all()
     }
     return render(request,'doctors.html',dict_doc)

def department(request):
    dict_dept={
         'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)


def contact(request):
    if request.method == 'POST':
        messages.success(request, 'Thank you for contacting us! We will reach out to you soon.') 
        return redirect('contact')
    return render(request, 'contact.html')









