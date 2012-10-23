# coding:utf-8
from mock import Mock
from django.test import TestCase
from eventex.subscriptions.admin import Subscription, SubscriptionAdmin, admin


class MarkAsPaidTest(TestCase):
    def setUp(self):
        #Instanciando o Model Admin
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)

        #Populando o banco
        Subscription.objects.create(name='Victor Novais', cpf='12345678910',
                                    email='victorh.novaisr@gmail.com',)

    def test_has_action(self):
        'Admin must contain actions'
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        'Mark all as paid'
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())