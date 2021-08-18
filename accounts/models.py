from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
from PIL import Image
from django.db.models.signals import post_save

def user_directory_path_profile(instance, filename):
    profile_picture_name = 'user/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name

def user_directory_path_banner(instance, filename):
    profile_picture_name = 'user/{0}/banner.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name

VERIFICATION_OPTIONS=(
    ('unverified', 'unverified'),
    ('verified', 'verified')
)

class User(AbstractUser):
    stripe_costumer_id = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(default='users/user_default_profile.png', upload_to=user_directory_path_profile)
    banner= models.ImageField(default='users/user_default_bg.jpg', upload_to=user_directory_path_banner)
    verified = models.CharField(max_length=10, choices=VERIFICATION_OPTIONS, default='unverified')
    coins= models.DecimalField(max_digits=19, decimal_places=2, default=0, blank=False)
    date_created=models.DateField(auto_now_add=True)

    #user info:
    location=models.CharField(max_length=10, null=True, blank=True)
    url=models.CharField(max_length=80, null=True, blank=True)
    birthday=models.DateField(null=True, blank=True)
    bio=models.TextField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

def create_user_pofile(sender, instance, created, **kwards):
    if created:
        Profile.objects.create(user=instance)

def save_user_pofile(sender, instance, **kwards):
    instance.profile.save()

post_save.connect(create_user_pofile, sender=User)
post_save.connect(save_user_pofile, sender=User)