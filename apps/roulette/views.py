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

def goBack(request):
    return redirect ('/')

def loginReg(request):
    return render(request, 'loginReg.html')

def newUser(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/loginReg')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name = request.POST["first_name"],
                                        last_name = request.POST["last_name"],
                                        email = request.POST["email"],
                                        username=request.POST['email'],
                                        password=pw_hash)
        return redirect(f'/dashboard/{new_user.id}')
    return redirect ('/dashboard')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/loginReg')
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/dashboard')
            # return redirect(f"/dashboard/{request.session['user_id']}")

def dashboard(request):
    return render (request, 'dashboard.html')

def editFaves(request):
    return redirect ('/dashboard')
<<<<<<< HEAD
=======

# def optionsSubmit(request):
#     return HttpResponse('It worked!')
>>>>>>> 0ef22677624b524e7634f950e89823cd65d8676b
