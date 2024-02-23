from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserCustom, Profile


@receiver(post_save, sender=UserCustom)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            name=instance.first_name + ' ' + instance.last_name,
            user=instance
        )
