from rest_framework import serializers
from .models import Projectroles

# class ProjectrolesSerializers(serializers.Serializer):
#     description = serializers.CharField(max_length=None)
#     member = serializers.IntegerField(source="member.id") 
#     project = serializers.IntegerField(source="project.id") 
#     creator = serializers.ReadOnlyField(source="creator.id")

#     def create(self, validated_data):
#         return Projectroles.objects.create(**validated_data)

class ProjectrolesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projectroles
        fields = ['id', 'description', 'member', 'project', 'creator']
        read_only_fields = ['id','creator']

    def create(self, validated_data):
        return Projectroles.objects.create(**validated_data)

class ProjectrolesDetailSerializers(ProjectrolesSerializers):
    def update(self, instance, validated_data):
            instance.description = validated_data.get('description', instance.description)
            instance.member = validated_data.get('member', instance.member)
            instance.save()
            return instance