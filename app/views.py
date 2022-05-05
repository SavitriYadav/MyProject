from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'app/base.html')

def home(request):
    return render(request, 'app/home.html')    

def aboutus(request):
    return render(request, 'app/aboutus.html')

def contact(request):
    return render(request, 'app/contact.html')

def stephen(request):
    return render(request, 'app/stephen.html')

def vanita(request):
    return render(request, 'app/vanita.html')

def swapnil(request):
    return render(request, 'app/swapnil.html')

def pritam(request):
    return render(request, 'app/pritam.html')

def vfx(request):
    return render(request, 'app/vfx.html')
