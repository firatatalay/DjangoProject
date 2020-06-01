from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from place.models import Category
from home.models import UserProfile, Setting
from user.forms import ProfileUpdateForm, UserUpdateForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)

    context = {'category': category,
               'profile': profile,
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
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        setting = Setting.objects.first()
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
            'setting': setting,
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
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        setting = Setting.objects.first()
        return render(request, 'change_password.html', {
            'form': form, 'category': category, 'setting': setting
        })