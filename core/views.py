from django.shortcuts import render, redirect, HttpResponseRedirect
from user_feedback.forms import FeedbackForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from user_feedback.models import Feedback, Reply
from django.shortcuts import get_object_or_404


def home(request):
    form = FeedbackForm()
    return render(request, 'home.html', {"form": form})


def capabilities(request):
    return render(request, 'capabilities.html')


def price(request):
    return render(request, 'price.html')


def send(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeedbackForm()
            return render(request, 'home.html', {"form": form, "Success": True})
        else:
            form = FeedbackForm()
            return render(request, 'home.html', {"form": form, "Success": False})


def reply_feedback(request, pk):
    if request.method == 'POST':
        try:
            feedback = get_object_or_404(Feedback, pk=pk)
            subject = "test_mail"
            email_from = settings.EMAIL_HOST_USER
            message = request.POST["id_send_feedback"]
            recipient_list = [feedback.email]
            # send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            reply = Reply(text=message, feedback=feedback)
            reply.save()
            messages.add_message(request, messages.SUCCESS, "Відповідь відправлена!")
            return HttpResponseRedirect(reverse('admin:user_feedback_feedback_changelist'))
        except:
            messages.add_message(request, messages.ERROR, "Сталася помилка!")
            return HttpResponseRedirect(reverse('admin:user_feedback_feedback_changelist'))
