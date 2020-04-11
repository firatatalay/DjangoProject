from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Setting


def index(request):
    setting = Setting.objects.first()
    context = {'setting': setting, 'page':'home'}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.first()
    context = {'setting': setting, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def iletisim(request):
    setting = Setting.objects.first()
    context = {'setting': setting, 'page':'iletisim'}
    return render(request, 'iletisim.html', context)