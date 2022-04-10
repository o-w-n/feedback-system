from django.forms import ModelForm
from .models import Feedback
from employees.models import Employee
from projects.models import Project
from django import forms


class FeedbackForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control  text-area',
            'rows': 7,
            'cols': 30,
            'placeholder': 'Текст повідомлення'
        }

    ), required=True)

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'aria-describedby': 'emailHelp',
            'placeholder': 'Email'
        }
    ), required=False)

    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all().order_by("name"),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'

            }
        ),

        empty_label="Співробітник",
        required=False,
    )

    project = forms.ModelChoiceField(
        queryset=Project.objects.all().order_by("name"),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        empty_label="Процес",
        required=False,
        label='Проект'
    )

    class Meta:
        model = Feedback
        fields = ['text', 'employee', 'project', 'email', "rating"]
