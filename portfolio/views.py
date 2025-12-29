from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.

def home(request):
    success = request.GET.get('success') =='1'
    return render(request,'home.html',{'success':success})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def projects(request):
    return render(request,'projects.html')

def submission(request):
    data = {
        'name':request.POST.get('name'),
        'email':request.POST.get('email'),
        'subject':request.POST.get('subject'),
    }
    
    return render(request,'csuccess.html');
    
    # return redirect('portfolio:home')
    # return redirect('/portfolio/?success=1')
    
    # return JsonResponse(data)