from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.


def home(request):
    if request.method == "POST":
        message_name = request.POST['fullName']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        print(message_name + "\n", message_email + "\n", message_subject)
        send_mail(
            "New Message from Portfolio Website",
            "Sender Email: " + message_email + "\n" +
            message_subject,  # message
            message_email,  # from email
            ['adalbertogarcia133@gmail.com']
        )
    return render(request, 'base/home.html')
