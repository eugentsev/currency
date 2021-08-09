from django.contrib import admin
from currency.models import Source, ContactUs
# Register your models here.


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'source_url',
    )

    list_filter = (
        'name',
    )


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
    )

    fields = [
        'subject',
        'email_from',
        'message',
    ]

    list_filter = (
        'subject',
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Source, SourceAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
