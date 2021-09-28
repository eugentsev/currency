from django.db import models
from currency import model_choices as mch


class Source(models.Model):
    source_url = models.CharField(max_length=225)
    name = models.CharField(max_length=64)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=64)
    message = models.CharField(max_length=512)


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)
    type = models.CharField(max_length=3, choices=mch.RATE_TYPES) # noqa


class ResponseLog(models.Model):
    status_code = models.PositiveSmallIntegerField()
    path = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    request_method = models.CharField(max_length=4, choices=mch.REQUESTS_METHOD)
    response_time = models.PositiveSmallIntegerField(
        help_text='in milliseconds'
    )
