# from django.shortcuts import render
from django.http import HttpResponse

from currency.models import ContactUs
# Create your views here.


def hello_world(request):
    return HttpResponse('Hello world!')


def contactus_list(request):
    contacts = ContactUs.objects.all()

    result = []

    for contact in contacts:
        result.append(
            f'ID: {contact.id} ',
            f'Email: {contact.email_from} ',
            f'Subject: {contact.subject} ',
            f'Message: {contact.message}'
        )

    return HttpResponse(str(result))
