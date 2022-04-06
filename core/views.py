from django.shortcuts import render, redirect
from user_feedback.forms import FeedbackForm
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    form = FeedbackForm()
    return render(request, 'home.html', {"form": form})

def send(request):
    # subject = "test_mail"
    # email_from = settings.EMAIL_HOST_USER
    # message = "test_message"
    # recipient_list = ["ya.orient@gmail.com"]
    # send_mail(subject, message, email_from, recipient_list, fail_silently=False)

    if request.method == 'POST':

        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeedbackForm()
            return render(request, 'home.html', {"form": form, "Success": True})
        else:
            form = FeedbackForm()
            return render(request, 'home.html', {"form": form, "Success": False})

def reply_feedback(request):
    if request.method == 'POST':
        reply = request.POST["id_send_feedback"]
        print(reply)
        return redirect('home')



