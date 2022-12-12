from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import *

# Register your models here.
admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(EventFile)