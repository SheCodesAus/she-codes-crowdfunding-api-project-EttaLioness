from rest_framework import serializers
from .models import Project, Pledge, CATEGORIES

class PledgeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']

# class PledgeSerializers(serializers.Serializer):
    # id = serializers.ReadOnlyField()
    # amount = serializers.FloatField()
    # comment = serializers.CharField(max_length=200)
    # anonymous = serializers.BooleanField()
    # supporter = serializers.CharField(max_length=200)
    # project_id = serializers.IntegerField() #drf id making from the project variable in model

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
    owner = serializers.ReadOnlyField(source="owner.id") # when serialise we insert id of owner from model
    category = serializers.ChoiceField(choices = CATEGORIES)

    def create(Self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializers(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance