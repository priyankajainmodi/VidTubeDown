from django.shortcuts import render
import requests
import sys
import os
from subprocess import run,PIPE
def page(request):
    return render(request,'link.html')
def output(request):      
    data=requests.get('https://codeforces.com/api/user.rating?handle=priyankajainmodi')
    print(data.text)
    data=data.text
    return render(request,'link.html',{'data':data})
def audio_mp3(request):
    inp=request.POST.get('param')
    fn = os.path.join(os.path.dirname(__file__), 'audio_mp3.py')
    out=run([sys.executable,fn,inp ],shell=False,stdout=PIPE)
    print(out)
    return render(request,'ret2.html',{'data1':out.stdout})
def high_res(request):
    inp=request.POST.get('param')
    fn = os.path.join(os.path.dirname(__file__), 'video_highest_res.py')
    out=run([sys.executable,fn,inp ],shell=False,stdout=PIPE)
    print(out)
    return render(request,'return.html',{'data1':out.stdout})
def low_res(request):
    inp=request.POST.get('param')
    fn = os.path.join(os.path.dirname(__file__), 'video_lowest_res.py')
    out=run([sys.executable,fn,inp ],shell=False,stdout=PIPE)
    print(out)
    return render(request,'return.html',{'data1':out.stdout})