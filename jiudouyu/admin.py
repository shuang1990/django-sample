from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone','real_name','identity_card', 'status_code', 'created_at')
    search_fields = ('phone','identity_card')
    list_filter = ('status_code',)
    ordering = ('id',)
    fields = ('status_code', 'note')

#admin.site.register(User, UserAdmin)