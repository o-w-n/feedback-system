from django.contrib import admin
from django.urls import path

from . import views

# from user_feedback.admin import myafs_admin_site

admin.site.site_header = "ASF Administration"
admin.site.site_title = "Anonymous System Feedback"
admin.site.index_title = "Dashboard"

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('send', views.send, name='send'),
    path('reply_feedback/<int:pk>', views.reply_feedback, name='reply_feedback'),
    path('admin/', admin.site.urls),
    path('price/', views.price, name='price'),
    path('capabilities/', views.capabilities, name='capabilities'),
]
