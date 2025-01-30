from django.shortcuts import render
from .forms import CarbonFootprintForm

def calculate_footprint(request):
    return render(request, 'calculator/calculate_footprint.html')# {'form': form, 'result': result})

def causes(request):
    return render(request, 'calculator/causes.html') 

def about(request):
    return render(request, 'calculator/causes.html')# Or another template path as necessary

def features(request):
    return render(request, 'calculator/causes.html')

def index(request):
    return render(request, 'calculator/index.html')