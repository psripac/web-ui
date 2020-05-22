from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request, 'coolui/index.html')

def contactView(request):
    return render(request, 'coolui/contact.html')

def projectView(request):
    return render(request, 'coolui/project.html')