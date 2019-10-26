from django.shortcuts import render



def application(request):
    return render(request, 'index/application.html')

