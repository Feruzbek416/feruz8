from django.shortcuts import render
from .models import *
# Create your views here.
def Clas1(request):
    Class = Clas.objects.all()
    return render(request,'schoolap/allclass.html',{'Class':Class})

def Clas2(request,title):
    Obj = Clas.objects.get(title=title)

    return render(request,'schoolap/class.html',{'Obj':Obj})

def Clas3(request):
    return render(request,'schoolap/test.html')