from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Subscription

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'avatar', 'date_of_birth', 'date_joined', 'is_active']

class SubscriptionSerializer(serializers.ModelSerializer):
    subscriber_username = serializers.CharField(source='subscriber.username', read_only=True)
    subscribed_to_username = serializers.CharField(source='subscribed_to.username', read_only=True)

    class Meta:
        model = Subscription
        fields = ['id', 'subscriber', 'subscriber_username', 'subscribed_to', 'subscribed_to_username', 'created_at']
        read_only_fields = ['id', 'created_at', 'subscriber']
