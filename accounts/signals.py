from django.db.models.signals import post_save
from .models import MyUser, Profile
from django.dispatch import receiver
import pysnooper



@receiver(post_save, sender = MyUser)
def create_profile (sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        print(instance)
        user_profile = Profile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

@receiver(post_save, sender = MyUser)
def save_profile (sender, instance, **kwargs):
    instance.profile.save()