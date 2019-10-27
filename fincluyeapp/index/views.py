from django.shortcuts import render




def application(request):
    return render(request, 'index/dashboard.html')

def new(request):
    return render(request, 'index/new.html')

def pendant(request):
    return render(request, 'index/pendant.html')

def success(request):
    return render(request, 'index/success.html')


