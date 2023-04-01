from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'name', 'tc', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'tc')}),
        ('permission', {'fields': ('is_admin',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'tc', 'password', 'password2')
        }),
    )

    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(EventFile)
admin.site.register(CompletionCertificateTemplate)
admin.site.register(MeritCertificateTemplate)
admin.site.register(ContributedCompletionCertificates)
admin.site.register(ContributedMeritCertificates)
admin.site.register(ParticipantAlbum)
