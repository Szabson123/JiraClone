from rest_framework import serializers
from .models import ToDoItem, ToDoList


class ToDoItemSerializer(serializers.ModelSerializer):
    to_do_list = serializers.SerializerMethodField()
    class Meta:
        model = ToDoItem
        fields = ['id', 'to_do_list', 'name', 'done']
        
    def get_to_do_list(self, obj):
        return obj.to_do_list.name if obj.to_do_list.name else None
        
        
class ToDoListSerializer(serializers.ModelSerializer):
    to_do_item = ToDoItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = ToDoList
        fields = ['id', 'name', 'description', 'to_do_item']
        
        