from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, UserInvitationViewSet, TaskViewSet, StatusViewSet, UserTaskViewSet

router = DefaultRouter()

router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'(?P<project_id>\d+)/inv_user', UserInvitationViewSet, basename='inv_user')
router.register(r'(?P<project_id>\d+)/task', TaskViewSet, basename='task')
router.register(r'(?P<project_id>\d+)/status', StatusViewSet, basename='status')
router.register(r'(?P<task_id>\d+)/add_user_to_task', UserTaskViewSet, basename='task_inv_user')

urlpatterns = [
    path('', include(router.urls))
]
