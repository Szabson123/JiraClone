from django.test import TestCase
from base.models import ToDoList, ToDoItem


class ToDoListModelTest(TestCase):
    def setUp(self) -> None:
        self.item = ToDoList.objects.create(
            name='Test Name',
            description='Test Description'
        )
    
    def test_to_do_list_creation(self):
        self.assertEqual(self.item.name, 'Test Name')
        self.assertEqual(self.item.description, 'Test Description')
        self.assertEqual(str(self.item), 'Test Name')
        
        
class ToDoItemModelTest(TestCase):
    def setUp(self) -> None:
        self.to_do_list = ToDoList.objects.create(
            name='Test Name',
            description='Test Description'
        )
        self.to_do_item = ToDoItem.objects.create(
            name = 'Test Item',
            done = False,
            to_do_list = self.to_do_list
        )
    
    def test_to_do_item_creation(self):
        self.assertEqual(self.to_do_item.name, 'Test Item')
        self.assertEqual(self.to_do_item.done, False)
        self.assertEqual(self.to_do_item.to_do_list, self.to_do_list)
        self.assertEqual(str(self.to_do_item), 'Test Item')
    
    def test_reverse_relation(self):
        item = self.to_do_list.to_do_item.all()
        self.assertIn(self.to_do_item, item)
        
    def test_default_done_value(self):
        item = ToDoItem.objects.create(name='Default Name', to_do_list=self.to_do_list)
        self.assertEqual(item.done, False)
    
    def test_cascade_delete(self):
        self.to_do_list.delete()
        self.assertFalse(ToDoItem.objects.filter(id=self.to_do_item.id).exists())
