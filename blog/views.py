from django.shortcuts import render

def landing(request):
    return render(request, "blog/landing.html")

def portfolio(request):
    return render(request, "blog/1portfolio.html")

def partners(request):
    return render(request, "blog/2partners.html")

def aboutus(request):
    return render(request, "blog/3aboutus.html")

def contact(request):
    return render(request, "blog/4contact.html")





# Create your views here.
