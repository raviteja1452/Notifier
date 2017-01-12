from django.contrib import admin

# Register your models here.
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'display_date')
    search_fields = ['title', 'description', 'display_date']


admin.site.register(Notification, NotificationAdmin)
