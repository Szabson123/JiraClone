from django.contrib import admin
from .models import Project, UserProject, Status


admin.site.register(Project)
admin.site.register(UserProject)
admin.site.register(Status)
# Register your models here.
