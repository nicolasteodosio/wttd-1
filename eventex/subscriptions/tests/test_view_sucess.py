# -*- coding:utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from eventex.subscriptions.models import Subscription


class SucessTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Victor Hugo', cpf='12345678910',
                                        email='victor@gmail.com',
                                        phone='21-9999-9999')
        self.resp = self.client.get(reverse('subscriptions:sucess', args=[s.pk]))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_sucess.html')

    def test_context(self):
        'Context must be an Subscription Instance'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Make sure that the page was rendered'
        self.assertContains(self.resp, 'Victor Hugo')

class SucessViewNotFoundTest(TestCase):
    def test_not_found(self):
        response = self.client.get(reverse('subscriptions:sucess', args=[0]))
        self.assertEqual(404, response.status_code)
