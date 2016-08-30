from django.test import TestCase
from fjfundo.core.models import MyUser


class DashboardTest(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(email='user@email.com', password='senha@123')
        self.client.login(email='user@email.com', password='senha@123')
        self.response = self.client.get('/dashboard/')

    def test_get(self):
        """ GET/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use dashboard.html """
        self.assertTemplateUsed(self.response, 'dashboard.html')
