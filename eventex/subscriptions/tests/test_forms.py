# -*- coding:utf-8 -*-
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_from_has_fields(self):
        'The SubscriptionForm class must have this fields'
        form = SubscriptionForm()
        self.assertItemsEqual(['name','email','cpf','phone'], form.fields)
