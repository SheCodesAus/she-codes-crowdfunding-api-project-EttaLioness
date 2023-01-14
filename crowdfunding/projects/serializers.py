from rest_framework import serializers
from .models import Project, Pledge

class PledgeSerializers(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.FloatField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField() #drf id making from the project variable in model

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)#** unpacks the list into individual items

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField() #readOnly so users cant choose
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField(read_only=True)
    owner = serializers.CharField(max_length=200)

    def create(Self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializers(many=True, read_only=True)