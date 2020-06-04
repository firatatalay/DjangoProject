from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from place.models import Category, Comment, Place
from home.models import UserProfile, Setting
from user.forms import ProfileUpdateForm, UserUpdateForm
from content.models import Content, Menu, CImages, ContentForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    setting = Setting.objects.first()
    footerrandompostimages = Place.objects.all().order_by('?')[:8]
    menu = Menu.objects.all()
    context = {'category': category,
               'profile': profile,
               'setting': setting,
               'footerrandompostimages': footerrandompostimages,
               'menu': menu
               }
    return render(request, 'userprofile.html',context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profiliniz başarıyla güncellendi!')
            return HttpResponseRedirect('/user/update')
    else:
        menu = Menu.objects.all()
        category = Category.objects.all()
        footerrandompostimages = Place.objects.all().order_by('?')[:8]
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        setting = Setting.objects.first()
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
            'setting': setting,
            'footerrandompostimages': footerrandompostimages,
            'menu': menu
        }
        return render(request, 'user_update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz Başarıyla Değiştirilmiştir!')
            return HttpResponseRedirect('/user/password')
        else:
            messages.warning(request, 'Please' + str(form.errors))
            return HttpResponseRedirect('/user/password')

    else:
        menu = Menu.objects.all()
        category = Category.objects.all()
        footerrandompostimages = Place.objects.all().order_by('?')[:8]
        form = PasswordChangeForm(request.user)
        setting = Setting.objects.first()
        return render(request, 'change_password.html', {
            'form': form,
            'category': category,
            'setting': setting,
            'footerrandompostimages': footerrandompostimages,
            'menu': menu
        })

@login_required(login_url='/login') #login kontrolü
def comments(request):
    menu = Menu.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id, status='True')
    category = Category.objects.all()
    footerrandompostimages = Place.objects.all().order_by('?')[:8]
    setting = Setting.objects.first()
    context = {
        'category': category,
        'comments': comments,
        'footerrandompostimages': footerrandompostimages,
        'setting': setting,
        'menu': menu
    }
    return render(request, 'comments.html', context)

@login_required(login_url='/login')
def deletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.warning(request, 'Yorumunuz Silindi.')
    return HttpResponseRedirect('/user/comments')



@login_required(login_url='/login')
def contents(request):
    category = Category.objects.all()
    menu = Menu.objects.all()
    current_user = request.user
    contents = Content.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'menu': menu,
        'contents': contents
    }
    return render(request, 'contents.html', context)

@login_required(login_url='/login')
def addcontent(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Content()
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            # data.category = form.cleaned_data['category']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save()
            messages.success(request, 'Başarıyla işlem gerçekleşti')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.warning(request, 'Content Form Error' + str(form.errors))
            return HttpResponseRedirect('/user/addcontent')

    else:
        category = Category.objects.all()
        menu = Menu.objects.all()
        form = ContentForm()
        context = {
            'menu': menu,
            'category': category,
            'form': form,
        }
        return render(request, 'addcontent.html', context)

@login_required(login_url='/login')
def editcontent(request, id):
    content = Content.objects.get(id=id)
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Güncelleme Başarıyla gerçekleştirildi')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.success(request, 'News Form Error:' + str(form.errors))
            return HttpResponseRedirect('/user/editcontent' + str(id))
    else:

        category = Category.objects.all()
        menu = Menu.objects.all()
        form = ContentForm(instance=content)
        news = {
            'menu': menu,
            'category': category,
            'form': form,
        }
        return render(request, 'addcontent.html', news)

@login_required(login_url='/login')
def deletecontent(request, id):
    current_user = request.user
    Content.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, ' News deleted..')
    return HttpResponseRedirect('/user/contents')

