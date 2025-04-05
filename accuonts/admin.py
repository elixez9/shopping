from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreateForm, ChangePasswordForm
from .models import User, OtpCode


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')


class UserAdmin(BaseUserAdmin):
    form = ChangePasswordForm
    add_form = UserCreateForm  #برای استفاده همزمان از دو فرم
    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'password')}),
        ('permissions', {'fields': ('is_admin', 'is_active', 'last_login')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'password')}),
        ('permissions', {'fields': ('is_admin', 'is_active', 'last_login')}),

    )
    search_fields = ('email', 'phone_number')  #جستجو کاربر از طریق ایمیل
    ordering = ('email',)  #دیته بندی کردن افراد از طریق ایمیل انها
    filter_horizontal = ()


admin.site.unregister(Group)  #غیر فعال کردن ریجستر جنگو
admin.site.register(User, UserAdmin)
