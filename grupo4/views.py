from django.shortcuts import render
from models import *

# Create your views here.

def grupo4(request):    
    return render(request, 'base.html', {})

def personas_list(request):
    personas = Persona.objects.all()
    return render(request, 'lista.html', {'personas': personas})
