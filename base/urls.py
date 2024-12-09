from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoListViewSet, ToDoItemViewSet

router = DefaultRouter()

router.register('to_do_list', ToDoListViewSet, basename='to_do_list')
router.register('(?P<to_do_list_id>\d+)/to_do_item', ToDoItemViewSet, basename='to_do_item')

urlpatterns = [
    path('', include(router.urls)),
]
