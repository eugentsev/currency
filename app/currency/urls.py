from django.urls import path

from currency.views import (
    ContactUsListView, RateListView,
    SourceListView, SourceCreateView,
    SourceDetailsView, SourceUpdateView,
    SourceDeleteView, ContactUsCreateView,
    RateDetailsView, RateUpdateView,
    RateDeleteView, RateCreateView,
)

app_name = 'currency'

urlpatterns = [

    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/details/<int:pk>/', SourceDetailsView.as_view(), name='source-details'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
    path('contactus/list/', ContactUsListView.as_view(), name='contactus-list'),
    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus-create'),
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/details/<int:pk>/', RateDetailsView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
]
