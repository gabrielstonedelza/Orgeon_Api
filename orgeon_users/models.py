from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image

DeUser = settings.AUTH_USER_MODEL

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def get_username(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="profile_user")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png")
    cover_pic = models.ImageField(blank=True, default='coverdefault.jpg', upload_to='cover_photos')
    fullname = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=100, blank=True, default='An employee of Orgeon of stars')
    bio = models.CharField(max_length=200, default='Just a music lover', blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def user_profile_pic(self):
        if self.profile_pic:
            return "127.0.0.1" + self.profile_pic.url

        return ''

    def user_cover_pic(self):
        if self.cover_pic:
            return "127.0.0.1" + self.cover_pic.url

        return ''