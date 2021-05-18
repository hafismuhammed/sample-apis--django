from django.db import models
from django.contrib.auth.models import User


def upload_to(instance, filename):
    return 'user/{filename}'.format(filename=filename)

class Blogs(models.Model):
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class UserImages(models.Model):
    image = models.ImageField(upload_to=upload_to, null=False, blank=False)
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)

