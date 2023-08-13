from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE,)
    profile_pic = models.ImageField(upload_to='profile_pics', default='default.png', blank=False, null=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=75, blank=True)
    dob = models.DateField(blank=True, null=True)
    joined_date = models.DateTimeField(default=timezone.now,editable=False)
    update_at = models.DateTimeField(auto_now=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Jsondata(models.Model):
    end_year = models.CharField(max_length=255, blank=True)
    intensity = models.CharField(max_length=255, blank=True)
    sector = models.CharField(max_length=255, blank=True)
    topic =  models.CharField(max_length=255, blank=True)
    insight =  models.CharField(max_length=255, blank=True)
    url = models.URLField(blank=True)
    region =  models.CharField(max_length=255, blank=True)
    start_year = models.CharField(max_length=255,blank=True)
    impact = models.CharField(max_length=255, blank=True)
    added = models.CharField(max_length=255, blank=True)
    published = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    relevance = models.CharField(max_length=255, blank=True)
    pestle = models.CharField(max_length=255, blank=True)
    source = models.CharField(max_length=255, blank=True)
    title = models.TextField(max_length=5000, blank=True)
    likelihood = models.CharField(max_length=255, blank=True)
    
    def __str_(self):
        return self.country