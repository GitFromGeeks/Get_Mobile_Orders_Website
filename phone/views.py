from django.shortcuts import render


def phoneview(request):
    return render(request,'phone.html')