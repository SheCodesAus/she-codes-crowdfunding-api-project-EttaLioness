from rest_framework import serializers
from .models import Project, Pledge, CATEGORIES
#from datetime import datetime, timedelta 
#added for end_date
from users.serializers import CustomUserSerializer #added for innovation star link
from projectroles.serializers import ProjectrolesSerializers


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
    # project = serializers.IntegerField() #drf id making from the project variable in model

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)#** unpacks the list into individual items

class PledgeDetailSerializer(PledgeSerializers):
    # id = serializers.ReadOnlyField()
    # amount = serializers.FloatField()
    # comment = serializers.CharField(max_length=None)
    # supporter = serializers.ReadOnlyField(source='supporter.id')
    # anonymous = serializers.BooleanField
    # project = serializers.ReadOnlyField()

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance
        
class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField() #readOnly so users cant choose
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField(read_only=True)#(auto_now_add=True)    
    end_date = serializers.DateTimeField(read_only=True)
    owner = serializers.ReadOnlyField(source="owner.id") # when serialise we insert id of owner from model
    category = serializers.ChoiceField(choices = CATEGORIES)
    total_stars = serializers.ReadOnlyField() #added for innovation star
    total_amount_pledged = serializers.ReadOnlyField() #added decorator for pledged
    
    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializers(many=True, read_only=True) 
    supporters_of_project = CustomUserSerializer(many=True, read_only=True)
    roles = ProjectrolesSerializers(many=True, read_only=True)#added to display project_roles
    innovation_star = CustomUserSerializer(many=True, read_only=True) #added for innovation star

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

    #do I want to update owner, date_created?