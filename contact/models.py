from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=221)
    number = models.FloatField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    created_date = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
