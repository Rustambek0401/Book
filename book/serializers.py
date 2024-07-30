from django.contrib.auth.models import User
from django.db.models import Avg
from django.db.models import Avg
from django.db.models.functions import Round
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from book.models import (Book,Author,Category )


class BookSerialize(serializers.ModelSerializer):
    author = serializers.CharField(source='auther.full_name', read_only=True)
    category = serializers.CharField(source='category.category_name', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
        extra_fields = ['author', 'category']




class AutherSerialize(serializers.ModelSerializer):
        class Meta:
            model = Author
            fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:

        model = Category
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username","password" ]

# Register
# class UserLoginSerializer(serializers.ModelSerializer):
#     id = serializers.PrimaryKeyRelatedField(read_only=True)
#     username = serializers.CharField(read_only=True)
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ["id", "username", "password"]
#

class UserRegisterSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name",
                  "last_name", "email", "password", "password2"]
        extra_kwargs = {
            'password': {"write_only": True}
        }

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            detail = {
                "detail": "User Already exist!"
            }
            raise ValidationError(detail=detail)
        return username

    def validate(self, instance):
        if instance['password'] != instance['password2']:
            raise ValidationError({"message": "Both password must match"})

        if User.objects.filter(email=instance['email']).exists():
            raise ValidationError({"message": "Email already taken!"})

        return instance

    def create(self, validated_data):
        passowrd = validated_data.pop('password')
        passowrd2 = validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        user.set_password(passowrd)
        user.save()
        Token.objects.create(user=user)
        return user