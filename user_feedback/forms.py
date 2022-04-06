from django.forms import ModelForm
from .models import Feedback
from employees.models import Employee
from projects.models import Project
from django import forms

class FeedbackForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'row': 5,
            'placeholder': 'Текст повідомлення'
        }

    ), required=True)

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'aria-describedby': 'emailHelp',
            'placeholder': 'Введіть адресу вашої електронної пошти'
        }
    ), required=False)

    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all().order_by("name"),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            }
        ),
        empty_label=" ",
        required=False,
    )

    project = forms.ModelChoiceField(
        queryset=Project.objects.all().order_by("name"),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            }
        ),
        empty_label=" ",
        required=False,
        label='Проект'
    )

    class Meta:
        model = Feedback
        fields = ['text', 'employee', 'project', 'email']

