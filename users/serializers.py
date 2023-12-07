from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'bio', 'profile_pic')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if not User.objects.filter(email=validated_data.get('email')).exists():
            user = User(
                email=validated_data.get('email'),
                username=validated_data.get('username'),
                first_name=validated_data.get('first_name', ''),
                last_name=validated_data.get('last_name', ''),
                bio=validated_data.get('bio', ''),
            )
            user.set_password(validated_data.get('password'))
            user.save()
        else:
            user = None
            print("El el correo ya existe jaja")
        return user