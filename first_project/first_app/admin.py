from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass

@admin.register(MailingList)
class MailinListAdmin(admin.ModelAdmin):
    pass

@admin.register(MailingService)
class MailingServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
