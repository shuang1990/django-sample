from django.contrib import admin
from django import forms
from .models import *

# 后台系统用户定义
from django.contrib.auth.admin import UserAdmin as AUserAdmin
from django.contrib.auth.models import User as AUser

class BackendUserAdmin(AUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('last_name',)


admin.site.unregister(AUser)
admin.site.register(AUser, BackendUserAdmin)

# admin widgets
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone', 'real_name', 'identity_card', 'status_code')
        widgets = {
            'note': forms.Textarea(attrs={'cols': 20, 'rows': 4}),
            'status_code': forms.RadioSelect,
        }


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone','real_name','identity_card', 'status_code', 'created_at', 'note')
    search_fields = ('phone','identity_card')
    list_filter = ('status_code',)
    list_editable = ('note', )
    #list_display_links = ('phone',)
    ordering = ('-id',)
    fields = ('phone','real_name','identity_card', 'status_code', 'note')
    form = UserForm
    class Meta:
        model = User


#admin.site.register(User, UserAdmin)

class InvestModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_id','user_id','cash', 'created_at')
    search_fields = ('project_id','user_id')
    list_filter = ('project_id', 'user_id',)
    ordering = ('-id',)
    fields = ('project_id', 'user_id')
    class Meta:
        model = Invest

admin.site.register(Invest, InvestModelAdmin)

