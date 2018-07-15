from django.shortcuts import render, get_object_or_404
from .models import Hall


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
         'exhibits': h.exhibits.filter(images__isnull=False)
         }
    )


def propose(request):
    return render(
        request,
        'propose.html'
    )


def hall_list(request):
    halls = Hall.objects.all()
    return render(
        request,
        'hall_list.html',
        {'halls': halls}
    )