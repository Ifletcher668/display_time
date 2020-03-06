from django.shortcuts import render, redirect
from time import strftime, localtime, gmtime
import pytz 

def index(request): 
    context = {
        "date": strftime("%d-%m-%Y", localtime()),
        "time": strftime("%H:%M %p", gmtime())
    }

    return render(request, "index.html", context)