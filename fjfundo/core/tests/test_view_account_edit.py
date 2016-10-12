from django.test import TestCase
from fjfundo.core.models import MyUser
from fjfundo.core.forms import EditAccountForm
from django.shortcuts import resolve_url as r


class AccountEditTest(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(email='user@email.com', password='senha@123')
        self.client.login(email='user@email.com', password='senha@123')
        self.response = self.client.get(r('account_edit', id=self.user.pk))

    def test_get(self):
        """ GET/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use edit_account.html """
        self.assertTemplateUsed(self.response, 'account_edit.html')

    def test_csrf(self):
        """ html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_html(self):
        """ Html must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 16)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="text"', 12)
        self.assertContains(self.response, 'type="submit"')

    def test_has_form(self):
        """ Context must have a LoginForm form"""
        form = self.response.context['form']
        self.assertIsInstance(form, EditAccountForm)

    def test_context(self):
        """User must be in context"""
        user = self.response.context['user']
        self.assertIsInstance(user, MyUser)

    def test_has_field(self):
        """ Form must have 14 fields"""
        form = self.response.context['form']
        self.assertSequenceEqual(['email', 'cpf', 'identidade', 'nome',
                                  'logradouro', 'numero', 'complemento', 'bairro',
                                  'cidade', 'uf', 'cep', 'fone1', 'fone2'],
                                 list(form.fields))



