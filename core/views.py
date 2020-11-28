from django.shortcuts import render

from core.models import Task


def read(request):
    objects = Task.objects.all()
    context = {'objects': objects}
    return render(request, 'read.html', context)
