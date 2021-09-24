import debug_toolbar
# from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import urls

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('currency/', include('currency.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path(r'silk/', include('silk.urls', namespace='silk')),
]
