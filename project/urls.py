from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, UserInvitationViewSet

router = DefaultRouter()

router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'(?P<project_id>\d+)/inv_user', UserInvitationViewSet, basename='inv_user')

urlpatterns = [
    path('', include(router.urls))
]
