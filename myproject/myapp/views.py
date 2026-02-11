from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
