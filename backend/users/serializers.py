from tokenize import Comment

from rest_framework import serializers
from backend.users.models import UserProfile, Companies
from django.contrib.auth.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class DisplayUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'availability', 'age', 'phone', 'skills')


class DisplayCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('user', 'company_user', 'company_name_type')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        UserProfile.objects.create(user=user, user_type=3)
        return user


class CompanySerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    print("company serializer")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        company_user = super(CompanySerializer, self).create(validated_data)
        print(str(company_user))
        company_user.set_password(validated_data['password'])
        company_user.save()
        Companies.objects.create(company_user=company_user, company_name_type=2)
        return company_user
