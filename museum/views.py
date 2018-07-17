from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from museum.helpers import country_name
from museum.models import Hall, Exhibit, Proposal

from watson import search as watson


def index(request):
    h_min = Hall.objects.order_by('number').first()

    return render(
        request,
        'index.html',
        {'min': h_min.number}
    )


def hall(request, hall_number):
    h = get_object_or_404(Hall, number=hall_number)
    h_min = Hall.objects.order_by('number').first()
    h_max = Hall.objects.order_by('number').last()
    h_prev = Hall.objects.filter(number__lt=h.number).order_by('number').last()
    h_next = Hall.objects.filter(number__gt=h.number).order_by('number').first()

    return render(
        request,
        'hall.html',
        {'hall': h,
         'prev': h_prev.number if hasattr(h_prev, 'number') else h.number,
         'next': h_next.number if hasattr(h_next, 'number') else h.number,
         'min': h_min.number,
         'max': h_max.number,
         'exhibits': h.exhibits.filter().filter(images__isnull=False).order_by('order_number').distinct(),
         'all_halls': Hall.objects.all()
         }
    )


def propose(request):
    if request.method == "POST":
        try:
            if request.POST['name']:
                name = request.POST['name']
            else:
                raise KeyError('Введите имя')
            if request.POST['description']:
                description = request.POST['description']
            else:
                raise KeyError('Введите описание')

            email = request.POST['email']
        except KeyError as e:
            messages.add_message(request, messages.WARNING, str(e))
            return render(request,
                          'propose.html')
        else:
            proposal = Proposal(name=name, message=description, email=email)
            proposal.save()
            messages.add_message(request, messages.SUCCESS, "<b>Спасибо!</b> Ваше предложение было отправлено")
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(
            request,
            'propose.html'
        )


def exhibit(request, e_id):
    exh = get_object_or_404(Exhibit, id=e_id)
    try:
        country = country_name(exh.country)
    except KeyError:
        country = ''
    return render(
        request,
        'exhibit_modal.html',
        {'e': exh,
         'country': country}
    )


def hall_list(request):
    halls = Hall.objects.all()
    return render(
        request,
        'hall_list.html',
        {'halls': halls}
    )


def search(request):
    query = request.GET.get('q', '')
    if query:
        results = watson.filter(Exhibit, query)
    else:
        results = Exhibit.objects.none()

    return render(
        request,
        'search.html',
        {'exhibits': results,
         'query': query}
    )
