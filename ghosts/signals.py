from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from ghosts.models import GhostUser


@receiver(post_save, sender=get_user_model())
def create_ghost_profile(sender, instance, created, **kwargs):
    if created:
        GhostUser.objects.create(user=instance)
