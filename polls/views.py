from django.http import HttpResponse
from django.shortcuts import render
from . import models


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def time(request):
    context = {
        "time": models.get_current_time()
    }
    return render(request, 'time.html', context)