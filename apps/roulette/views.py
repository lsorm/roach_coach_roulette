from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import *
import bcrypt

def index(request):
    return render(request, 'index.html')

def optionsDisplay(request):
    return render (request, 'options.html')

def roulett(request):
    return redirect ('/resultsDisplay')

def resultsDisplay(request):
    return render (request, 'results.html')

def viewInfo(request):
    return render (request, 'view.html')

def GoBack(request):
    return redirect ('/')

def loginReg(request):
    return render(request, 'loginReg.html')

def newUser(request):
    return redirect ('/dashboard')

def dashboard(request):
    return render (request, 'dashboard.html')

def editFaves(request):
    return redirect ('/dashboard')

