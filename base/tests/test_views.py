from django.test import TestCase
from base.views import ToDoListViewSet, ToDoItemViewSet
from rest_framework.test import APITestCase
from base.models import ToDoItem, ToDoList
from rest_framework import status

class ToDoListViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.to_do_list = ToDoList.objects.create(name='Test List', description='Test_description')
        self.to_do_item = ToDoItem.objects.create(name='Test Item', to_do_list=self.to_do_list)
        self.basic_url = '/list/to_do_list/'
        self.change_done_url = '/list/to_do_list/item_set_true_false/'
    
    def test_get_empty_to_do_list(self):
        ToDoList.objects.all().delete()
        response = self.client.get(self.basic_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        
    def test_get_query_set(self):
        response = self.client.get(self.basic_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.to_do_list.name)
        self.assertEqual(response.data[0]['description'], self.to_do_list.description)
        self.assertIn('id', response.data[0])
        
    def test_get_multi_items_query_set(self):
        adition_item = ToDoList.objects.create(name='Test List2', description='Test_description2')
        response = self.client.get(self.basic_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], self.to_do_list.name)
        self.assertEqual(response.data[1]['name'], adition_item.name)
    
    def test_get_to_do_item_in_list(self):
        aditional_item = ToDoItem.objects.create(name='Test Item2', to_do_list=self.to_do_list)
        response = self.client.get(self.basic_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 1)
        
        to_do_items = response.data[0]['to_do_item']
        self.assertEqual(len(to_do_items), 2)
        
        self.assertEqual(to_do_items[0]['name'], self.to_do_item.name)
        self.assertEqual(to_do_items[1]['name'], aditional_item.name)
    
    def test_post_to_do_list(self):
        data = {
            'name': 'new test List',
            'description': 'Test TEst tets'
        }
        response = self.client.post(self.basic_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertIn('id', response.data)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['description'], data['description'])
        
        self.assertTrue(ToDoList.objects.filter(name='new test List').exists())
    
    def test_post_not_all_elements(self):
        data = {
            'name': 'new test test List'
        }
        response = self.client.post(self.basic_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(ToDoList.objects.filter(name='new test test List').exists())
    
    def test_post_item_to_list(self):
        data = {
            'name': 'new test test List',
            'description': 'description',
            'to_do_item': [{'name': 'Test Item', 'done': False}]
        }
        
        response = self.client.post(self.basic_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(ToDoList.objects.filter(name='new test test List').exists())
        
    def test_post_change_done_to_true_false(self):
        item = ToDoItem.objects.create(name='New', done=False, to_do_list=self.to_do_list)
        
        response = self.client.post(self.change_done_url, {'id': item.id}, format='json')
        item.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], item.id)
        self.assertTrue(item.done)
        self.assertEqual(response.data['done'], item.done)

        response = self.client.post(self.change_done_url, {'id': item.id}, format='json')
        item.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], item.id)
        self.assertFalse(item.done)
        self.assertEqual(response.data['done'], item.done)


class ToDoItemViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.to_do_list = ToDoList.objects.create(name='Test List', description='Test_description')
        self.to_do_item = ToDoItem.objects.create(name='Test Item', to_do_list=self.to_do_list)
        self.url = f'/list/{self.to_do_list.id}/to_do_item/'
        
    def test_get_to_do_items(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 1)
        
        self.assertEqual(response.data[0]['name'], self.to_do_item.name)
        self.assertEqual(response.data[0]['to_do_list'], self.to_do_list.name)
        self.assertEqual(response.data[0]['done'], False)
    
    def test_post_to_do_items(self):
        data = {
            'name': 'Nowy',
            'to_do_list': self.to_do_list.id
        }
        
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertTrue(ToDoItem.objects.filter(name='Nowy').exists())
        self.assertEqual(response.data['to_do_list'], self.to_do_list.name)
        