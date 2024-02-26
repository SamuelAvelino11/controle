from django.shortcuts import render

# Create your views here.

def View_Order(request):
    return render(request, 'cad_ordem.html')

def View_login(request):
    return render(request, 'login.html')