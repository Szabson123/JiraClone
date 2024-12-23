from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework.permissions import IsAuthenticated

from .models import Project, UserProject, Status, Task
from .serializers import ProjectSerializer, UserProjectSerializerName, UserProjectSerializer, TaskSerializer, StatusSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        owner = self.request.user
        project = serializer.save(owner=owner)
        Status.objects.create(project=project, name="To Do")
        Status.objects.create(project=project, name="Done")
        Status.objects.create(project=project, name="Pending")
        

class UserInvitationViewSet(viewsets.ModelViewSet):
    serializer_class = UserProjectSerializer
    queryset = UserProject.objects.all()
    
    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(Project, id=project_id)
        invited_user = serializer.validated_data.get('user')
        
        if project.users.filter(id=invited_user.id).exists():
            raise ValidationError({"error": "This user already exists in this project"})

        if not project.owner == self.request.user:
            raise ValidationError({'error': 'You have no permission to inv people'})

        serializer.save(project=project)
        return super().perform_create(serializer)
    

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.none()
    serializer_class = TaskSerializer
    
    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(Project, id=project_id)
        serializer.save(project=project)
        return super().perform_create(serializer)
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        task = Task.objects.filter(project_id=project_id)
        return task
    

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.none()
    permission_classes = StatusSerializer
    
    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        project = get_object_or_404(Project, id=project_id)
        serializer.save(project=project)
        
    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        status = Status.objects.filter(project_id=project_id)
        return status