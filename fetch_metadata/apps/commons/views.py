from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, "common/home.html")

def about(request):
    return render(request, "common/about.html")