from django.test import TestCase
from fjfundo.core.forms import LoginForm


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """ GET/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use index.html """
        self.assertTemplateUsed(self.response, 'index.html')

    def test_html(self):
        """ Html must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="password"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """ html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have a LoginForm form"""
        form = self.response.context['form']
        self.assertIsInstance(form, LoginForm)

    def test_has_field(self):
        """ Form must have 2 fields"""
        form = self.response.context['form']
        self.assertSequenceEqual( ['email', 'password'], list(form.fields))
