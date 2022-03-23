# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def make_many_teachers(apps, schema_editor):
    Student = apps.get_model('school', 'Student')

    for student in Student.objects.all():
        student.teachers.add(student.teacher)


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_student_teachers_alter_student_teacher'),
    ]

    operations = [
        migrations.RunPython(make_many_teachers),
    ]