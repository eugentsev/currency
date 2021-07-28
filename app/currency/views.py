from django.shortcuts import render
# from django.http import HttpResponse


from currency.models import ContactUs, Rate
# Create your views here.


def index(request):
    return render(request, 'index.html')


def contactus_list(request):
    contacts = ContactUs.objects.all()

    context = {
        'contactus_list': contacts
    }

    return render(request, 'contactus_list.html', context=context)


def rate_list(request):
    rates = Rate.objects.all()

    context = {
        'rate_list': rates
    }

    return render(request, 'rate_list.html', context=context)