from django.shortcuts import render
from .forms import *
# Create your views here.
def formcomment(req):
    nashaforma = UserComment()#пустая форма
    data={'form123':nashaforma}
    print(1)
    if req.POST:#отправил форму
        nashaforma = UserComment(req.POST)#форма с данными
        data={'form123':nashaforma}
        print(2)
        if nashaforma.is_valid():
            print(3)
            k1 = nashaforma.cleaned_data.get('name')
            k2 = nashaforma.cleaned_data.get('comment')
            # k1 = req.POST.get('name')
            data={'name':k1,'com':k2}
            return render(req, 'finish.html' ,data)

    return render(req, 'forma.html', data)

def index(req):
    data={}
    return render(req, 'index.html', data)

def finish(req):
    data={}
    return render(req, 'finish.html', data)

def formtel(req):
    nashaforma = UserTel()
    data={'form234':nashaforma}
    if req.POST:#отправил форму
        nashaforma = UserTel(req.POST)#форма с данными
        data={'form234':nashaforma}
        if nashaforma.is_valid():
            print(3)
            k1 = nashaforma.cleaned_data.get('name')
            k2 = nashaforma.cleaned_data.get('tel')
            k3 = nashaforma.cleaned_data.get('tarif')
            # k1 = req.POST.get('name')
            data={'name':k1,'tel':k2, 'tarif':k3}
            return render(req, 'finish.html' ,data)
    return render(req, 'forma.html', data)