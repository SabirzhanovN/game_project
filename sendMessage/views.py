from django.shortcuts import render, redirect
from .service import send_message_bot
from django.contrib import messages as ms

# Create your views here.


def send_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        msg = f'Заявка с сайта:\nName - {name}\nEmail - {email}\nphone - {phone}\nmessage - {message}'
        send_message_bot(msg)

        ms.success(request, 'Message successfully send')

        return redirect('index')