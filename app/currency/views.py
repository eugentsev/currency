from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from currency.models import ContactUs, Rate, Source
from currency.forms import SourceForm, ContactUsForm
from django.urls import reverse_lazy
# from django.core.mail import send_mail

from currency.tasks import contactus_task
# Create your views here.


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_list.html'


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_create.html'


class SourceDetailsView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_update.html'


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_delete.html'


class ContactUsCreateView(CreateView):
    queryset = ContactUs.objects.all()
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:contactus-list')
    template_name = 'contactus_create.html'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email_from = form.cleaned_data['email_from']

        full_email_body = f'''
        Email From: {email_from}
        Body: {message}'''

        contactus_task.apply_async(args=(subject, ), kwargs={'body': full_email_body})

        return super().form_valid(form)
