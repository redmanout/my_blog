from django.shortcuts import render, redirect
from .forms import UserRegForm
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
    return render(request, 'users/profile.html')
