from django.shortcuts import render

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