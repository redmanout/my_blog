from django.shortcuts import render, redirect
from .forms import UserRegForm, ProfileImageForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан')
            return redirect('home')
    else:
        form = UserRegForm()
    return render(
        request,
        'users/reg.html',
        {
            'title': 'Страница регистрации',
            'form': form
        })


@login_required
def profile(request):
    if request.method == "POST":
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUseForm = UserUpdateForm(request.POST, instance=request.user)

        if profileForm.is_valid() and updateUseForm.is_valid():
            updateUseForm.save()
            profileForm.save()
            messages.success(request, f'Ваш аккаунт успешно обновлен')
            return redirect('profile')
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUseForm = UserUpdateForm(instance=request.user)

    data = {
        'profileForm': profileForm,
        'updateUseForm': updateUseForm
    }
    return render(request, 'users/profile.html', data)
