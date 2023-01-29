from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.http import Http404
from .models import Projectroles
from .serializers import ProjectrolesSerializers, ProjectrolesDetailSerializers
from .permissions import IsCreatorOrReadOnly 

class ProjectrolesList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #built in django to allow only logged in
    
    def get(self, request):
        roles = Projectroles.objects.all()
        if request.data.get("project"):
            roles = roles.filter(project = request.data.get("project"))
        if request.data.get("creator"):
            roles = roles.filter(creator = request.data.get("creator"))
        serializer = ProjectrolesSerializers(roles, many=True) #get list of many roles not one
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectrolesSerializers(data=request.data)# use the data that was given from user
        if serializer.is_valid():#built in serializer checks info given is ok, as expected
            serializer.save(creator=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProjectrolesDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsCreatorOrReadOnly
    ]

    def get_object(self, pk):
        try:
            # return Project.objects.get(pk=pk) #passing the input in as an attribute
            roles = Projectroles.objects.get(pk=pk)
            self.check_object_permissions(self.request, roles)
            return roles
        except Projectroles.DoesNotExist:
            raise Http404 #means resource does not exit, user did something wrong
    def get(self, request, pk):
        roles = self.get_object(pk)
        serializer = ProjectrolesDetailSerializers(roles)
        return Response(serializer.data)

    def put(self, request, pk):
        roles = self.get_object(pk)
        data = request.data
        serializer = ProjectrolesDetailSerializers(
            instance = roles,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
            ####Added what happens if not valid like above

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)