from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import ToDoItem, ToDoList
from.serializers import ToDoItemSerializer, ToDoListSerializer


class ToDoListViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoListSerializer
    queryset = ToDoList.objects.all()
    
    @extend_schema(request={'application/json': {'type': 'object', 'properties': {'id': {'type': 'integer',}},}})
    @action(detail=False, methods=['POST'])
    
    def item_set_true_false(self, request):
        item_id = self.request.data.get('id')
        item = get_object_or_404(ToDoItem, id=item_id)
        
        item.done = not item.done
        item.save()
        
        return Response({'id': item.id, 'done': item.done}, status=status.HTTP_200_OK)
    

class ToDoItemViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoItemSerializer
    queryset = ToDoItem.objects.none()
    
    def get_queryset(self):
        to_do_list_id = self.kwargs.get('to_do_list_id')
        return ToDoItem.objects.filter(to_do_list_id=to_do_list_id)
    
    def perform_create(self, serializer):
        to_do_list_id = self.kwargs.get('to_do_list_id')
        to_do_list = get_object_or_404(ToDoList, id=to_do_list_id)
        serializer.save(to_do_list=to_do_list)
    
    def perform_update(self, serializer):
        to_do_list_id = self.kwargs.get('to_do_list_id')
        to_do_list = get_object_or_404(ToDoList, item=to_do_list_id)
        serializer.save(to_do_list=to_do_list)
        