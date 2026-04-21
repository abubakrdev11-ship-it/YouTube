from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager

# Create your models here.
class CustomUserModel(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
class Subscription(models.Model):
    subscriber = models.ForeignKey(CustomUserModel, related_name='subscriptions', on_delete=models.CASCADE)
    subscribed_to = models.ForeignKey(CustomUserModel, related_name='subscribers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    unique_together = ('subscriber', 'subscribed_to')

    def __str__(self):
        return self.subscriber

