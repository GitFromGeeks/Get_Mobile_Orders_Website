from django.shortcuts import render

def indexview(request):
    return render(request,"index.html")

def aboutview(request):
    return render(request,"about.html")