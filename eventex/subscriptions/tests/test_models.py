#-*- coding:utf-8 -*-
from datetime import datetime
from django.db.utils import IntegrityError
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Victor Hugo Novais',
            cpf = '12345678910',
            email = 'victorh.novaisr@gmail.com',
            phone = '21-99999999',
        )

    def test_create(self):
        'Subscription must have name, cpf, email and phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_created_at(self):
        'The field created_at must be the current datetime'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Victor Hugo Novais', unicode(self.obj))

    def test_paid_default_value_is_false(self):
        'By default, paid must be false'
        self.assertEqual(False,self.obj.paid)

class SubscriptionPostTest(TestCase):
    def setUp(self):
        'Setting up a valid post for tests'
        data = dict(name='Victor Hugo Novais', cpf='12345678910',
                    email='victorh.novaisr@gmail.com', phone='21-9999-9999')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        'Valid POST must redirect to sucess page'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        self.assertTrue(Subscription.objects.exists())




class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        'Creating an Instance of Subscription()'
        Subscription.objects.create(cpf='12345678910',
                                    email='victorh.novaisr@gmail.com')

    def test_cpf_is_unique(self):
        'CPF must be an unique field'
        s = Subscription(cpf='12345678910',)
        self.assertRaises(IntegrityError, s.save)

    def test_email_can_repeat(self):
        'Email is not unique anymore'
        s = Subscription.objects.create(name='Victor Hugo Novais',cpf='10987654321',
            email='victorh.novaisr@gmail.com')
        self.assertEqual(2, s.pk)