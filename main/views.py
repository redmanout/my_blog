from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .forms import MessageForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


def main(request):
    data = {
        'title': 'Mysite',
        'h1': 'Simple and convenient service',
        'h2': 'We do work quickly and efficiently'
    }
    return render(request, 'main/main.html', data)


def services(request):
    data = {
        'title': 'Services',
        'h2': 'Services page',
        'quickly_block': 'Quickly',
        'cheap_block': 'Сheap',
        'qualitatively_block': 'Qualitatively',
        'text': 'Lorem ipsum nam: cursus sit risus tellus vulputate ut nec, massa lectus maecenas justo eu, non mauris'
                ' commodo congue eros. Odio cursus fusce amet, sem gravida porta cursus, mattis leo eros, enim congue'
                ' mattis metus congue porta — leo a — maecenas, malesuada. Tellus ornare at bibendum integer amet'
                ' mattis fusce cursus ultricies nec metus in.'
    }
    return render(request, 'main/services.html', data)


def contacts_send(request):
    subject = 'topic_letter'
    plain_message = 'text_message'
    from_email = 'email'
    to = 'vladimirkotov1115@gmail.com'
    if request.method == 'GET':
        form = MessageForm()
    elif request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Сообщение успешно отправлено')
            try:
                send_mail(subject, from_email, plain_message, [to])
            except BadHeaderError:
                return HttpResponse('Ошибка')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос')
    return render(request, 'main/contacts.html', {'form': form})


def success_send(request):
    return HttpResponse('Успешно')
