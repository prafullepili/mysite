from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'barns/login.html',)

def dashboard(request):
    context = {'dashboard':'sub_modules_active'}
    return render(request,'barns/dashboard.html',context)

def barn(request):
    context = {'barns':'sub_modules_active'}
    return render(request,'barns/barns.html',context)

def barn_details(request):
    context = {'dashboard':'sub_modules_active'}
    return render(request,'barns/barn_details.html',context)

def devices(request):
    context = {'devices':'sub_modules_active'}
    return render(request, 'barns/devices.html',context)
