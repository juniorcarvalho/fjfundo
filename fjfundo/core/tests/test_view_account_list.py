from django.test import TestCase
from fjfundo.core.models import MyUser


class AccountEditTest(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(email='user@email.com', password='senha@123',
                                               nome='Usuario teste', fone1='1234567890')
        self.client.login(email='user@email.com', password='senha@123')
        self.response = self.client.get('/account_list/')

    def test_get(self):
        """ GET/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use edit_account.html """
        self.assertTemplateUsed(self.response, 'account_list.html')

    def test_context(self):
        """User must be in context"""
        user = self.response.context['user']
        self.assertIsInstance(user, MyUser)

    def test_html(self):
        contents = [
            'Usuario teste',
            'user@email.com',
            '1234567890',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)
