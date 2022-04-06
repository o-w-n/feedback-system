from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('send', views.send, name='send'),
    path('reply_feedback', views.reply_feedback, name='reply_feedback'),

]
