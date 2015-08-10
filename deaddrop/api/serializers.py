from rest_framework import serializers
import models


class RecipientSerializer(serializers.Serializer):
    id = serializers.EmailField()
    email = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=12)


class SecretSerializer(serializers.Serializer):
    recipient = RecipientSerializer()
    content_delivery_channel = serializers.ChoiceField(choices=models.CHANNEL_TYPES)
    key_delivery_channel = serializers.ChoiceField(choices=models.CHANNEL_TYPES)
    sender_id = models.CharField(max_length=models.DEFAULT_MAX_LENGTH)
    sender_reply_address = models.CharField(max_length=models.DEFAULT_MAX_LENGTH)
