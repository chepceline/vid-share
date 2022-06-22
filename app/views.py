from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.urls import reverse
from django.http import HttpResponseRedirect
    
def homepage(request):
    title = 'Welcome to vidshare'

    context = {
        'title':title,
    }
    return render(request,'all-pages/homepage.html', context=context)
