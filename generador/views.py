from django.http import HttpResponse
from django.shortcuts import render
import random
from .models import UserCreado
# Create your views here.

def home(request):
   return render(request, 'generador/home.html')

def password(request):
   characters = list('abcdefghijklmnopqrstuvwxyz')
   generated_password = ''
   longuitud = int(request.GET.get('length'))
   
   if request.GET.get('uppercase'):
      characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
      
   if request.GET.get('characters'):
      characters.extend(list('!@#$%^&*()'))
      
   if request.GET.get('numbers'):
      characters.extend(list('0123456789'))
  
   for x in range(longuitud):
      generated_password += random.choice(characters)
    
   nombre = request.GET.get('name')
   email = request.GET.get('correo')
   print(nombre)
   print(email)
     
   UserCreado.objects.create(
      username=nombre,
      email=email,
      password=generated_password,
   )
      
   
   return render(request, 'generador/password.html',{'password': generated_password})