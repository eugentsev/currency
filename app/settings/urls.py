from django.contrib import admin
from django.urls import path

from currency.views import hello_world, contactus_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactus/list/', contactus_list),
    # currency
    path('hello-world/', hello_world),
]
