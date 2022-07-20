from django.shortcuts import render
from django.http import HttpResponse
from .models import Foundation
from .models import Description

# Create your views here.

def home(request):
    description = Description.objects.all()
    context = {'descriptions': description}
    return render(request, 'base/home.html', context)

def foundation(request,pk):
    descriptions = Description.objects.get(id=pk)
    context = {'descriptions': descriptions}
    return render(request, 'base/foundations.html',context)

def donate(request):
    return render(request, 'base/donate.html')


