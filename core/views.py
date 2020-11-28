from django.shortcuts import render, redirect, get_object_or_404

from core.models import Task
from core.forms import FormTask


def read(request):
    objects = Task.objects.all()
    context = {'objects': objects}
    return render(request, 'read.html', context)


def create(request):
    if request.method == 'POST':
        form = FormTask(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('details', id=task.id)
    form = FormTask()
    return render(request, 'form.html', context={'form': form})


def details(request, id):
    object = get_object_or_404(Task, id=id)
    return render(request, 'details.html', context={'object': object})


def delete(request, id):
    object = get_object_or_404(Task, id=id)
    object.delete()
    return redirect('read')
