from django.views.generic import ListView
from django.shortcuts import render
from school import models

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    object_list = list(models.Student.objects.all().order_by(ordering))
    context = {'object_list': object_list}
    return render(request, template, context)
