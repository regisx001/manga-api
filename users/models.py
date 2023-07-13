import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from django.conf import settings


from django.contrib.admin.decorators import display
from django.template.loader import get_template


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=400)
    email = models.EmailField('Email Address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,   related_name='profile')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.user.username + " profile"

    @display(description='Preview')
    def avatar_preview(self):
        return get_template('img_preview.html').render({
            'field_name': 'avatar',
            'src': self.avatar.url if self.avatar else None,
        })


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    if kwargs["created"]:
        UserProfile.objects.create(user=instance)


@receiver(pre_save, sender=UserProfile)
def delete_old_avatars_onUpdate(sender, instance, **kwargs):
    old_avatar = sender.objects.filter(user=instance.user).first() or None
    if not old_avatar:
        return
    if old_avatar.avatar == "":
        return
    os.remove(f"media/{old_avatar.avatar}")


@receiver(pre_delete, sender=User)
def delete_old_avatars_onDelete(sender, instance, **kwargs):
    old_avatar = instance.profile.avatar
    if old_avatar == "":
        return
    os.remove(f"media/{old_avatar}")
