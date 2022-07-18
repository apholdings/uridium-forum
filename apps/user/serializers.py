from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields =[
            'id',
            'account',
            'email',
            'username',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'get_picture',
            'get_banner',
            'location',
            'url',
            'birthday',
            'profile_info',
            'age_limit',
            'verified',
        ]