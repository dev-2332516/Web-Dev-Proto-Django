from django.db.models.signals import post_delete, post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver

import os
from django.core.files.storage import default_storage

from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()


# ---------- Image/File housekeeping ----------

def _delete_file(path: str) -> None:
    if not path:
        return
    try:
        if default_storage.exists(path):
            default_storage.delete(path)
    except Exception:
        # Silent fail to avoid breaking save/delete lifecycle
        pass


def _get_field_file_path(instance, field_name: str) -> str:
    file_field = getattr(instance, field_name, None)
    if file_field and getattr(file_field, 'name', ''):
        return file_field.name
    return ''


def _handle_replacement(sender, instance, field_name: str):
    if not instance.pk:
        return
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return
    old_path = _get_field_file_path(old_instance, field_name)
    new_path = _get_field_file_path(instance, field_name)
    if old_path and old_path != new_path:
        _delete_file(old_path)


@receiver(pre_save, sender=UserProfile)
def replace_profile_picture_on_update(sender, instance, **kwargs):
    _handle_replacement(sender, instance, 'picture')