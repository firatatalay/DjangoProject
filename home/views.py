import json

from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormMessage, ContactFormu
from place.models import Place, Category, Images, Comment
from home.forms import SearchForm


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
    comments = Comment.objects.filter(place_id=id, status='True').order_by('create_at')[:]
    context = {'place': place,
               'category': category,
               'randomplaces': randomplaces,
               'images': images,
               'comments': comments,
               }
    return render(request, 'placedetail.html', context)




def place_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            places = Place.objects.filter(title__icontains=query)
            context = { 'places': places,
                        'category': category,
                        }
            return render(request,'places_search.html',context)

    return HttpResponseRedirect('/')



# def place_search_auto(request):
#     if request.is_ajax():
#         q = request.GET.get('term', '')
#         places = Place.objects.filter(title__icontains=q)
#         results = []
#         for rs in places:
#             place_json = {}
#             place_json = rs.title
#             results.append(place_json)
#         data = json.dumps(results)
#     else:
#         data = 'fail'
#     mimetype = 'application/json'
#     return HttpResponse(data, mimetype)

def place_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        places = Place.objects.filter(title__icontains=q)
        results = []
        for r in places:
            results.append(r.title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)