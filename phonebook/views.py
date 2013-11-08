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
                request.session['loggedin'] = True
                return HttpResponseRedirect("/contact/")
    
    elif request.session['loggedin'] != False:
        return HttpResponseRedirect("/contact/")
        
    else :
        request.session['loggedin'] = False
        return render_to_response("login.html", {}, context_instance=RequestContext(request))

def Contact(request):
    
    if request.session['loggedin'] == False :
        return HttpResponseRedirect("/logout/")
    
    else :
        name = request.user.id
        print name
        contact = contacts.objects.filter(user=name)
        name = request.user
        return render_to_response("contact.html", {'contacts':contact,'user':name}, context_instance=RequestContext(request))

def AddContact(request):
    if request.method == 'POST':
        form = addcontact(request.POST or None)
        form.user = request.user
        if form.is_valid():
            print "Form valid"
            cmodel = form.save(commit=False)
            #This is where you might chooose to do stuff.
            #cmodel.name = 'test1'
            cmodel.user = request.user
            cmodel.save()
            return HttpResponseRedirect('/contact/')
        
        else :
            error = "Some Error Occured while adding your contact. Please check the errors and re-Add the contact. Dont worry you dont have to type the details again. Django gives it for you always."
            return render(request, "addcontact.html", {'form': form,'error':error})
    
    else :
        form = addcontact()
        relation = relations.objects.all()
        return render(request, "addcontact.html", {'form': form,'relation':relation})

def EditContact(request):
    if request.method == 'POST':
        value = request.POST['name']
        print value
    return HttpResponseRedirect('/contact/')
    
def Logout(request):
    request.session['loggedin'] = False
    return HttpResponseRedirect("/login/")