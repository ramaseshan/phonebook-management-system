from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from phonebook.models import *
from phonebook.forms import addcontact

def Login(request):
    c = {}
    c.update(csrf(request))
    
    if request.method== 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['loggedin'] = username
                return HttpResponseRedirect('/contact/')
    
    elif request.session != "":
        return HttpResponseRedirect('/contact')
        
    else :
        request.session['loggedin'] = ""
        return render_to_response("login.html", {}, context_instance=RequestContext(request))

def Contact(request):
    
    if request.session['loggedin'] == "" :
        return HttpResponseRedirect("/login/")
    
    else :
        contact = contacts.objects.all()
        return render_to_response("contact.html", {'contacts':contact}, context_instance=RequestContext(request))
    
def AddContact(request):
    if request.method == 'POST':
        print "Inside POST"
        form = addcontact(request.POST or None)
        if form.is_valid():
            print "Form valid"
            cmodel = form.save()
            print cmodel
            #This is where you might chooose to do stuff.
            #cmodel.name = 'test1'
            cmodel.save()
            return HttpResponseRedirect('/contact/')
    else :
        form = addcontact()
        return render(request, "addcontact.html", {'form': form})
        

def Logout(request):
    request.session['loggedin'] = ""
    return HttpResponseRedirect("/login/")