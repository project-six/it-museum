from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(
        request,
        'index.html'
    )


def hall(request, hall_number):
    return render(
        request,
        'hall.html',
        {'hall_number': hall_number}
    )
