from django.contrib import admin
from .models import Contact, ComtactMe
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


admin.site.register(Contact, ContactAdmin)
admin.site.register(ComtactMe)