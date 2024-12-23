from rest_framework import serializers
from .models import Project, UserProject, Status, Task


class UserProjectSerializer(serializers.ModelSerializer):
    user_projects = serializers.SerializerMethodField()
    is_accepted = serializers.BooleanField(read_only=True)
    class Meta:
        model = UserProject
        fields = ['id', 'user', 'user_projects', 'role', 'is_accepted']

    def get_user_projects(self, obj):
        return obj.project.name or None


class UserProjectSerializerName(serializers.ModelSerializer):
    user_in_project = serializers.SerializerMethodField()
    is_accepted = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = UserProject
        fields = ['user_in_project', 'role', 'is_accepted']

    def get_user_in_project(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}' 


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name', 'project']


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.SerializerMethodField()
    status_id = serializers.PrimaryKeyRelatedField(source='status', queryset=Status.objects.all(), write_only=True)
    status_name = serializers.CharField(source='status.name', read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'project', 'name', 'description', 'status_name', 'status_id']
        
    def get_project(self, obj):
        return obj.project.name
    
    def get_status(self, obj):
        return obj.status.name
    
    
class ProjectSerializer(serializers.ModelSerializer):
    project_owner = serializers.SerializerMethodField()
    users = UserProjectSerializerName(many=True, source='user_projects', read_only=True)
    tasks_all = TaskSerializer(many=True, source='tasks', read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'project_owner', 'description', 'users', 'tasks_all']
        
    
    def get_project_owner(self, obj):
        return f'{obj.owner.first_name} {obj.owner.last_name}'
    

