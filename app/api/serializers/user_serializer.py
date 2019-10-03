from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    password = CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'email')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if validated_data.get('password') != "null":
            instance.password = make_password(validated_data.get('password', instance.password))
        else:
            instance.password = instance.password

        instance.save()

        return instance