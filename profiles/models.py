from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='image')
    bio = models.TextField()
    email = models.EmailField(blank=True, null=True)
    number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    @property
    def full_name(self):
        name = []
        if self.user.first_name:
            name.append(self.user.first_name)
        if self.user.last_name:
            name.append(self.user.last_name)
        if name:
            full_name = ' '.join(name)
            return full_name
        return self.user


def profile_post_save(instance, sender, created, *args, **kwargs):
    if created:
        obj = Profile.objects.create(user=instance)
        obj.save()
        return obj
    return None


post_save.connect(profile_post_save, sender=User)

