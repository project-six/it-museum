import random

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
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


def hall(request, hall_number, exh_id=None):
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
         'all_halls': Hall.objects.all(),
         'open_exh': exh_id
         }
    )


def propose(request):
    if request.method == "POST":
        if not (request.POST['name'] and request.POST['description']):
            messages.add_message(request, messages.WARNING, str("Вы должны заполнить поля с именем и описанием"))
            return render(request,
                          'propose.html')

        name = request.POST['name']
        description = request.POST['description']
        email = request.POST['email']
        
        proposal = Proposal(name=name, message=description, email=email)
        proposal.save()
        messages.add_message(request, messages.SUCCESS, "<b>Спасибо!</b> Ваше предложение было отправлено")
        return HttpResponseRedirect(reverse('propose'))
    else:
        return render(
            request,
            'propose.html'
        )


def exhibit(request, e_id):
    exh = get_object_or_404(Exhibit, id=e_id)
    hall_number = exh.hall.number

    return redirect('hall', hall_number=hall_number, exh=exh)


def exhibit_data(request, e_id):
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


def search(request, exh_id=None):
    query = request.GET.get('q', '')
    if query:
        results = watson.filter(Exhibit, query)
    else:
        results = Exhibit.objects.none()

    print(exh_id)

    return render(
        request,
        'search.html',
        {'exhibits': results,
         'query': query,
         'open_exh': exh_id}
    )


def random_exh(request):
    exh = random.choice(Exhibit.objects.all())
    hall_number = exh.hall.number

    return redirect('hall', hall_number=hall_number, exh_id=exh.id)
