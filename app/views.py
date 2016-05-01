from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader

from .models import Email, User

# Create your views here.

def index(request):
    emails = Email.objects.filter(senderId="P8561044896590126190")
    context = {
            'emails': emails,
    }

    return render(request, 'app/index.html', context)

def detail(request, email_id):
    print(email_id)
    email = Email.objects.get(pk=email_id)
    sender = User.objects.get(pk=email.senderId)
    print(type(email))
    context = {
            'email': email,
            'sender': sender,
    }
    return render(request, 'app/detail.html', context)
