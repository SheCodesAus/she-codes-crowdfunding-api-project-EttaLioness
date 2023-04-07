from rest_framework import serializers
from .models import CustomUser
from django.utils import timezone #added
# from rest_framework.validators import UniqueValidator

class CustomUserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length=200) #added
    last_name = serializers.CharField(max_length=200) #added
    username = serializers.CharField(max_length=200)
#     username = serializers.CharField(max_length=100, validators=[
#         UniqueValidator(
#             queryset=CustomUser.objects.all(),
#             message=("Name already exists")
#         )
#     ]
# )
    date_joined = serializers.DateTimeField(read_only=True) #added
    email = serializers.EmailField()
    image = serializers.URLField(default = "https://i.postimg.cc/rm82XhCm/default-profile-image.png") #added
    bio = serializers.CharField(max_length=None) #added
    qualifications = serializers.CharField(max_length=None) #added
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
class CustomUserDetailSerializer(CustomUserSerializer):
    

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.image = validated_data.get('image', instance.image)
        instance.email = validated_data.get('email', instance.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.qualifications = validated_data.get('qualifications', instance.qualifications)
        instance.affiliate = validated_data.get('affiliate', instance.affiliate)
        # instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

# class ChangePasswordSerializer(serializers.Serializer):
#     model = CustomUser

#     """
#     Serializer for password change endpoint.
#     """
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)