from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from django.utils.html import mark_safe
from django.contrib.admin.decorators import display

from . import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


admin.site.unregister(Group)


@admin.register(Group)
class UserAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(models.UserProfile)
class UserProfileAdmin(ModelAdmin):
    readonly_fields = ["avatar_preview"]
    list_display = ["list_display_avatar", "list_display_name"]
    list_display_links = list_display

    @display(description="name")
    def list_display_name(self, obj):
        return mark_safe(f"<span style='font-size:1rem;font-weight:800'>Profile</span> : {obj.user} ")

    @display(description="avatar")
    def list_display_avatar(self, obj):
        if not obj.avatar:
            return mark_safe(f"<img src='http://atrilco.com/wp-content/uploads/2017/11/ef3-placeholder-image.jpg' width='50' height='50' />")
        return mark_safe(f"<img src='{obj.avatar.url}' width='50' height='50' />")
