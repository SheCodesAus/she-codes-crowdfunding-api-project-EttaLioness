from rest_framework import serializers
from .models import CustomUser
from django.utils import timezone #added

class CustomUserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length=200) #added
    last_name = serializers.CharField(max_length=200) #added
    username = serializers.CharField(max_length=200)
    date_joined = serializers.DateTimeField(default= timezone.now) #added
    email = serializers.EmailField()
    image = serializers.URLField(default = "https://i.postimg.cc/rm82XhCm/default-profile-image.png") #added
    bio = serializers.CharField(max_length=None, default = None) #added
    qualifications = serializers.CharField(max_length=None, default = None) #added
    affiliate = serializers.CharField(max_length=200) #added
    password = serializers.CharField(write_only = True)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password',]
#         read_only_fields = ['id', 'email', 'username',]

        # def create(self, validated_data):
        #     return CustomUser.objects.create_user(**validated_data)