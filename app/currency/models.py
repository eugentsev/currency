from django.db import models


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
    type = models.CharField(max_length=3) # noqa