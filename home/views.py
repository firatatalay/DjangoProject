from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormMessage, ContactFormu
from place.models import Place, Category, Images



def index(request):
    setting = Setting.objects.first()
    sliderdata = Place.objects.all()[:5]
    category = Category.objects.all()
    lastplaces = Place.objects.all().order_by('-id')[:5]
    randomplaces = Place.objects.all().order_by('?')[:4]
    mainrandomplacessmall = Place.objects.all().order_by('?')[:30]
    mainrandomplacesbig = Place.objects.all().order_by('?')[:10]


    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'category': category,
               'lastplaces': lastplaces,
               'randomplaces': randomplaces,
               'mainrandomplacessmall': mainrandomplacessmall,
               'mainrandomplacesbig': mainrandomplacesbig,
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


def place_detail(request, id, slug):
    category = Category.objects.all()
    place = Place.objects.get(pk=id)
    randomplaces = Place.objects.all().order_by('?')[:3]
    images = Images.objects.filter(place_id=id)
    context = {'place': place,
               'category': category,
               'randomplaces': randomplaces,
               'images': images,
               }
    return render(request, 'placedetail.html', context)





