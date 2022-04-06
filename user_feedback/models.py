from django.db import models

from employees.models import Employee
from projects.models import Project


class Feedback(models.Model):
    text = models.TextField(verbose_name='Текст')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                 blank=True, related_name="employees",
                                 verbose_name='Сотрудник', null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                blank=True, related_name="projects",
                                verbose_name='Проект', null=True)
    email = models.EmailField(blank=True, verbose_name='Почта')
    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'От {self.email}' if self.email else f'Для {self.employee}' or f'Для {self.project}'

    class Meta:
        ordering = ("email", )
