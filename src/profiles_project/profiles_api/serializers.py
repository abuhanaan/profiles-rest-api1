from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our API"""

    name = serializers.CharField(max_length=10)
    

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our own UserProfile object."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Creates and return a new user"""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name'])

        user.set_password(validated_data['password'])
        user.save()

        return user