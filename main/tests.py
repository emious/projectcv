# myapp/tests.py
import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import Project


class ProjectTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.item = Project.objects.create(id=999,
                                           name='Test Project',
                                           description='Test Desc',
                                           created_at=datetime.datetime.now(),
                                           updated_at=datetime.datetime.now())
        self.item_data = {"id": 10000,
                          "name": "New Project",
                          "description": "test",
                          'created_at': '2024-07-14T17:56:55.988319Z',
                          'updated_at': '2024-07-14T17:56:55.988319Z'}
        self.url = reverse('main:projects')

    def test_get_items(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_item(self):
        self.url = reverse('main:add_project')
        print(self.item_data)
        response = self.client.post(self.url, self.item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 2)
        self.assertEqual(Project.objects.get(id=response.data['id']).name, 'New Project')

    def test_get_item(self):
        response = self.client.get(reverse('main:view_project', args=[self.item.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)

    def test_update_item(self):
        updated_data = {"id": 10000, 'name': 'Updated Project', 'description': 'Updated Description'}
        response = self.client.put(reverse('main:update_project', args=[self.item.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(Project.objects.get(id=response.data['id']).name, 'Updated Project')

    def test_delete_item(self):
        response = self.client.delete(reverse('main:del_project', args=[self.item.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Project.objects.count(), 0)
