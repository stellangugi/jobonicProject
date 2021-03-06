from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import JobonicUser, UserProfile
from django.utils.translation import ugettext_lazy as _


class JobonicsUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'is_active')}),
        (_('Permissions'), {'fields': ('is_staff',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_created')}),
    )
    readonly_fields = ('date_created',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'first_name', 'last_name')
    list_filter = ()
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    filter_horizontal = []

admin.site.register(JobonicUser, JobonicsUserAdmin)
admin.site.register(UserProfile)
