from django.db import models
from user.models import CustomUser

class Project(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='project_owner')
    name = models.CharField(max_length=255)
    description = models.TextField()
    users = models.ManyToManyField(CustomUser, through='UserProject')


class UserProject(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE, related_name='user_projects')
    project = models.ForeignKey(Project, models.CASCADE, related_name='user_projects')
    role = models.CharField(max_length=255)
    is_accepted = models.BooleanField(default=False)
    

