from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("get_email", "employee", "project",)
    list_filter = ("email",)
    search_fields = ("email__startswith",)

    def get_email(self, obj):
        return obj.email or "---"
    # def created_at(self):
    #     return

