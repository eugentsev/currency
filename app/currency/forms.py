from django import forms

from currency.models import Source, ContactUs, Rate


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'name',
            'source_url',
        )


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'source',
            'type',
            'sale',
            'buy',
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message',
        )
