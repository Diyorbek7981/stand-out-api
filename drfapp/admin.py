from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'user_name',
        'is_confirmed',
        'age',
        'certificate',
        'phone_number',
        'role',
        'is_registered',
    )
    list_display_links = (
        'id',
        'first_name',
        'user_name',
        'phone_number',
        'age',
    )
    list_editable = ('is_confirmed',)
    list_filter = ('role', 'is_confirmed', 'certificate')
    search_fields = ('id', 'first_name', 'user_name', 'phone_number', 'certificate')
    ordering = ('-created_at',)
    list_per_page = 25
