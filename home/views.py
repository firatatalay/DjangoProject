from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormMessage, ContactFormu
from place.models import Place, Category


def index(request):
    setting = Setting.objects.first()
    sliderdata = Place.objects.all()[:5]
    category = Category.objects.all()
    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'category': category,
               }
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.first()
    category = Category.objects.all()
    context = {'setting': setting, 'page':'hakkimizda','category': category}

    return render(request, 'hakkimizda.html', context)

def iletisim(request):

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Teşekkürler, mesajınız alındı. En kısa sürece geribildirim alacaksınız.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.first()
    form = ContactFormu()
    category = Category.objects.all()
    context = {'setting': setting, 'form':form, 'category': category}
    return render(request, 'iletisim.html', context)


def category_places(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    places = Place.objects.filter(category_id=id)
    context = {'places': places,
               'category': category,
               'categorydata': categorydata
               }
    return render(request, 'places.html', context)





