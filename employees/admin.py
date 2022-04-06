from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")
    list_filter = ("name", "surname")
    search_fields = ("name__startswith", "surname__startswith")
