from django.contrib import admin
from django.urls import path

from currency.views import (
    contactus_list, index,
    rate_list, source_list,
    source_create, source_details,
    source_update, source_delete)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    path('source/list/', source_list),
    path('source/create/', source_create),
    path('source/details/<int:source_id>/', source_details),
    path('source/update/<int:source_id>/', source_update),
    path('source/delete/<int:source_id>/', source_delete),
    path('contactus/list/', contactus_list),
    path('rate/list/', rate_list),
]
