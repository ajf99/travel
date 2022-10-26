from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import person
def demo(request):
    obj=place.objects.all()
    obj1=person.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})
# def addiction(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})