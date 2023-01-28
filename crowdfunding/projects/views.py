from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer,ProjectDetailSerializer, PledgeSerializers, PledgeDetailSerializer
from django.http import Http404
from rest_framework import status, generics, permissions
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #built in django to allow only logged in
    
    def get(self, request):
        projects = Project.objects.all()
        if request.data.get("category"):
            projects = projects.filter(category=request.data.get("category"))
        if request.data.get("owner"):
            projects = projects,filter(owner=request.data.get("owner"))
        serializer = ProjectSerializer(projects, many=True) #get list of many projects not one
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)# use the data that was given from user
        if serializer.is_valid():#built in serializer checks info given is ok, as expected
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            # return Project.objects.get(pk=pk) #passing the input in as an attribute
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404 #means resource does not exit, user did something wrong
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance = project,
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

        #Look up try and accept in python


# class PledgeList(APIView):
#     def get (self, request):
#         pledges = Pledge.objects.all()
#         serializer = PledgeSerializers(pledges, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PledgeSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

class PledgeList(generics.ListCreateAPIView): #to create a read-write endpoint that lists all available Pledge instances
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializers
    permission_classes = [                             ###added for editing
        permissions.IsAuthenticatedOrReadOnly
    ]
    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)

class PledgeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [                             ###added for editing
        permissions.IsAuthenticatedOrReadOnly,
        IsSupporterOrReadOnly
    ]
    queryset = Pledge.objects.all()
    serializer_class = PledgeDetailSerializer
