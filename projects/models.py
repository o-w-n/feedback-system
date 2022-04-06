from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Проект')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("name",)
