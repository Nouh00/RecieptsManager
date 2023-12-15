from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Reciept

class ReceiptTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.reciept = Reciept.objects.create(
            user=self.user,
            store_name='Test Store',
            data_of_purchase='2023-01-01',
            item_list='Item 1, Item 2',
            total_amount=50.0
            )

    def test_reciept_list(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('reciepts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Store')
    def test_reciept_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('reciepts:reciept', args=[self.reciept.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['reciept'].store_name, 'Test Store')

    def test_reciept_create(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('reciepts:newReciept'), {
            'user':self.user,
            'store_name':'Test Store',
            'data_of_purchase':'2023-01-01',
            'item_list':'Item 1, Item 2',
           ' total_amount':50.0
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reciept.objects.last().store_name, 'Test Store')

    def test_reciept_update(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('reciepts:editReciept', args=[self.reciept.id]), {
            'user':self.user,
            'store_name':'Updated Receipt',
            'data_of_purchase':'2023-01-01',
            'item_list':'Item 1, Item 2',
           ' total_amount':50.0
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reciept.objects.get(id=self.reciept.id).store_name, 'Updated Receipt')

    def test_reciept_delete(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('reciepts:deleteReciept', args=[self.reciept.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reciept.objects.filter(id=self.reciept.id).count(), 0)

    def test_login_view(self):
        response = self.client.get(reverse('reciepts:login'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(reverse('reciepts:register'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('reciepts:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.client.session.get('_auth_user_id'))