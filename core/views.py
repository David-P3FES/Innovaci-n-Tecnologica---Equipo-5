# core/views.py

from django.shortcuts import render

def inicio(request):
    return render(request, 'core/home.html')  # <-- incluyendo subcarpeta

