from django.db import models


class ToDoList(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    

class ToDoItem(models.Model):
    to_do_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='to_do_item')
    name = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name