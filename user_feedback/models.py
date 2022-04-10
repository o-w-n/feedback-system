from django.db import models

from employees.models import Employee
from projects.models import Project


class Feedback(models.Model):
    text = models.TextField(verbose_name="Зворотній зв'язок")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                 blank=True, related_name="employees",
                                 verbose_name='Сотрудник', null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                blank=True, related_name="projects",
                                verbose_name='Проект', null=True)
    email = models.EmailField(blank=True, verbose_name='Email')
    rating = models.IntegerField(blank=True, verbose_name="Rating")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="дата")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'От {self.email}' if self.email else f'Для {self.employee}' or f'Для {self.project}'

    class Meta:
        ordering = ("-created_at", )

    def has_reply(self):
        return True if self.feedbacks.all() else False

    def get_reply(self):
        return self.feedbacks.all()[0].text if self.has_reply() else "Немає відповіді!"

class Reply(models.Model):
    text = models.TextField(verbose_name='Текст')
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE,
                                 blank=True, related_name="feedbacks",
                                 verbose_name='Відповідь на фідбек: ', null=True)
