from django.db.models.signals import post_save, pre_delete, pre_save
import os
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(pre_delete, sender=User)
def delete_profile_picture_on_delete(sender, instance, **kwargs):
    if instance.profile_picture and instance.profile_picture.path:
        if os.path.isfile(instance.profile_picture.path):
            os.remove(instance.profile_picture.path)

@receiver(pre_save, sender=User)
def delete_old_profile_picture_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return  # Skip if this is a new object

    try:
        old_file = Profile.objects.get(pk=instance.pk).profile_picture
    except Profile.DoesNotExist:
        return

    new_file = instance.profile_picture
    if old_file and old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)