from django.contrib import admin

from .models import Feedback
# from django.contrib.admin import AdminSite
# from django.utils.translation import ugettext_lazy

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("get_created_at", "text", "get_email", "employee", "project", "rating")
    list_filter = ("employee", "project", "rating")
    search_fields = ("email__startswith",)


    def get_email(self, obj):
        return obj.email or "anonymous"

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d %b %Y")


# class MyAfsAdminSite(AdminSite):
#     site_title = ugettext_lazy("fff")
#     site_header = ugettext_lazy("fff2")
#     index_title = ugettext_lazy("fff1")
#
# myafs_admin_site = MyAfsAdminSite()