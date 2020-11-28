from django import forms
from core.models import Task


class FormTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
