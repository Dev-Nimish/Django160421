from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def page1(request):
    return render(request,"sample1.html", context ={'name':'Nimish'})

def page2(request,data):
    return render(request,"sample2.html",context = {'data':data})

def page3(request):
    return render(request,"sample3.html")