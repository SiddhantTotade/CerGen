from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

# Register your models here.


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("id", "email", "first_name", "last_name",)
    fieldsets = (
        ("User Credentials", {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password", "password2"),
        },
    )

    search_fields = ("email",)
    ordering = ("email", "id")
    filter_horizontal = ()


admin.site.register(User, UserAdmin)