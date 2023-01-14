from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer,ProjectDetailSerializer, PledgeSerializers
from django.http import Http404
from rest_framework import status

class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True) #get list of many projects not one
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)# use the data that was given from user
        if serializer.is_valid():#built in serializer checks info given is ok, as expected
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class ProjectDetail(APIView):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk) #passing the input in as an attribute
        except Project.DoesNotExist:
            raise Http404 #resource does not exit, user did something wrong
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

        #Look up try and accept in python

class PledgeList(APIView):
    def get (self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializers(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )