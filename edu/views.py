
# Create your views here.
from distutils.command.config import config
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

import pyrebase
from django.http import HttpResponse

from .models import Destination1

config={
    'apiKey': 'AIzaSyC9kwIq6QN_8TSj8WV_3MzibXb5yPwOIg0',
    'authDomain': 'esp32demo-decdd.firebaseapp.com',
    'databaseURL': 'https://esp32demo-decdd-default-rtdb.asia-southeast1.firebasedatabase.app',
    'databaseURL': 'https://esp32demo-decdd-default-rtdb.asia-southeast1.firebasedatabase.app',
    'projectId': 'esp32demo-decdd',
    'storageBucket': 'esp32demo-decdd.appspot.com',
    'messagingSenderId': '12434325963',
    'appId': '1:12434325963:web:61d46d381f1e43b9e3364e'
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.

def index1(request):
    flag=0
    ref = int(request.POST["ref"])
    pas = int(request.POST["pass"])
    dets=Destination1.objects.all()
    for val in dets:
        if (val.id==ref and val.Password==pas):
            flag=1
            name=val.name
    if (flag):        
        return render(request,'index1.html',{'name':name,'flag':flag})
    else:
        return render(request,'index.html')
    
def index(request):
    return render(request,'index.html')

def About(request): 
    # send_mail(
    #             'Welcome Email',
    #             'You have been successfully login.',
    #             'okbye260@gmail.com',
    #             ['okbye260@gmail.com'],
    #             fail_silently=False,
    # )
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')


def result(request):
    dets=Destination1.objects.all()
    for val in dets:
            SSN = database.child('test').child('float').get().val()
            Voltage = database.child('test').child('Voltage').get().val()
            Current = database.child('test').child('int').get().val()
            if (val.id==SSN):
                return render(request,'result.html',{'dets':dets, 'Voltage':Voltage, 'Current':Current, 'Pow':Voltage*Current,'val':val})
        
    