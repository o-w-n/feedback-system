from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        ordering = ("name", "surname")
