from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=100)
    status = serializers.IntegerField(default=0)
    created_date = serializers.DateTimeField('user created date')

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.name = validated_data.get('name', instance.name)
        instance.password = validated_data.get('password', instance.password)
        instance.status = validated_data.get('status', instance.status)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.save()
        return instance