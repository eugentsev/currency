from django.contrib import admin
from django.urls import path

from currency.views import contactus_list, index, rate_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    path('contactus/list/', contactus_list),
    path('rate/list/', rate_list),
]
