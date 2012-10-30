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

    def test_cpf_is_digit(self):
        'CPF must only accept digits'
        form = self.make_validated_form(cpf='ABCD5678910')
        self.assertItemsEqual(['cpf'],form.errors)

    def test_email_is_optional(self):
        'Email is optional.'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_cpf(self):
        'Email and phone are optional, but one must be informed'
        form = self.make_validated_form(email='', phone='')
        self.assertItemsEqual(['__all__'], form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(name='Victor Hugo Novais', email='victorh.novaisr@gmail.com',
                    cpf='12345678910', phone='21-9999-9999')
        data.update(**kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form