from django.shortcuts import render
from forms import urlforms
from django.http import HttpResponseRedirect

from models import url
import datetime
import re
def home(request):
    h=''
    f=urlforms(request.POST)
    if request.method=='POST':
        if f.is_valid():   
            cd=f.cleaned_data 
            m=url.objects.filter(urlcode=cd['urlform']) 
            for each in m:
            
                h=each.hexcode
                print 'h',h
                return render(request,'home.html',{'f':f,'h':h})
            time=datetime.datetime.now()
            match=re.search('([\d]+)-([\d]+)-([\d]+)\s([\d]+):([\d]+):([\d]+).([\d]+)',str(time))
            if match:
                x=0
                for each in match.group(7):
                    x=x+int(each)
                y1,x=incr(match.group(2),x)
                for each in match.group(6):
                    x=x+int(each)
                y2,x=incr(match.group(1),x)
                y3,x=incr(match.group(3),x)
                y4,x=incr(match.group(4),x)
                y5,x=incr(match.group(5),x)
            h=dup(x+1,y1+y2+y3+y4+y5)
            x=x+1
         
            p=url(hexcode=h,urlcode=cd['urlform'])
            p.save()
    return render(request,'home.html',{'f':f,'h':h})   
def newu(request,uname):
    f=urlforms()
    m=url.objects.filter(hexcode=uname)
    for each in m:
        return HttpResponseRedirect('/'+'/'+each.urlcode+'/')
def incr(mg,y):
    a='abcdefghijklmnopqrstuvwxyz'
    for each in mg:
        y=y+int(each)
    while y>25:
        x=0
        for each in str(y):
            x=x+int(each)
            y=x
    n=a[y]
    return n,y
def dup(c,h):
    a='abcdefghijklmnopqrstuvwxyz'
   
    v=url.objects.filter(hexcode=h)
    for each in v:
        y1=a[c%25]
        y2=a[(c+1)%25]
        y3=a[(c+2)%25]
        y4=a[(c+3)%25]
        y5=a[(c+4)%25]
        return dup(c+1,y1+y2+y3+y4+y5)
    return h
