from django.shortcuts import render
from .forms import contactform
from .models import contactModel
# Create your views here.
def contactview(request):
 if request.method == 'POST':
  fm = contactform(request.POST)
  if fm.is_valid():
   nm = fm.cleaned_data['name']
   ph = fm.cleaned_data['phone']
   msg = fm.cleaned_data['message']
   con = contactModel(name=nm,phone=ph,message=msg)
   con.save()
   return render(request,'thankyou.html')
 else:
  fm = contactform()

 return render(request, 'contact.html', {'form':fm})
