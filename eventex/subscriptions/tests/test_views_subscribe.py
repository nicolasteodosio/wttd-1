# -*-coding:utf-8 -*-
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        'GET /inscricao/ must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Testing if the right template is beeing rendered'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        'Testing if the HTML contains the right number of tags'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'HTML must contain csfr token for validation'
        self.assertContains(self.resp,'csrfmiddlewaretoken')

    def test_has_form(self):
        'The subscription form must be included in the context of the view'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class  SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(name='Victor Hugo Novais', cpf='000000000012',
        email='victor', phone='21-9999-9999')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        'Invalid POST should not redirect'
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        'Form must contain errors'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'If there is an error, form must not save'
        self.assertFalse(Subscription.objects.exists())