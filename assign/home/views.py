from django.shortcuts import render
from .models import *
import hashlib
import base64

# Create your views here.

message=''

longurl2=''



def shorten_url( long_url):
    unique_value = hashlib.sha1(long_url.encode()).hexdigest()
    short_url = base64.urlsafe_b64encode(unique_value.encode())[:6].decode()

    return short_url


def index(request):
    shorturl=''
    longurl=''
    message=''
    urls=Url.objects.all()
    return render(request,'home.html',{
        "shorturl1":shorturl,
        'longurl2':longurl,
        'message':message,
        'urls':urls
    })


def encode(request):
    if request.method=='POST':
        longurl1=request.POST.get('longurl')
        shorturl1=''
        if(longurl1!=''):
            try:
                
                shorturl1=Url.objects.get(long_url=longurl1).short_url
            except:
                i=0
                while(i<=0):
                    try:
                        shorturl1=shorten_url(longurl1)
                        a=Url(long_url=longurl1,short_url=shorturl1)
                        a.save()
                        break
                    except:
                        i-=1
                    
        message=''
        urls=Url.objects.all()
        return render(request,'home.html',{
        "shorturl1":shorturl1,
        'longurl1':longurl1,
        'message':message,
        'urls':urls
        })
    
def decode(request):
    if request.method=='POST':
        shorturl2=request.POST.get('shorturl')
        longurl2=''
        if(shorturl2!=''):
            try:
                longurl2=Url.objects.get(short_url=shorturl2).long_url
                message=''
            except:
                message='This short url not created yet, so cannot decode..'
        urls=Url.objects.all()   
        return render(request,'home.html',{
        "shorturl2":shorturl2,
        'longurl2':longurl2,
        'message':message,
        'urls':urls
        })