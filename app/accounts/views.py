from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User
import requests


class MyProfileView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    fields = (
        'first_name',
        'last_name',
    )
    success_url = reverse_lazy('index')
    template_name = 'my-profile.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.request.user.id)
        return queryset
