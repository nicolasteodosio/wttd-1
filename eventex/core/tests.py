# -*- coding:utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class HomePageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('core:homepage'))

    def test_get(self):
        'GET / must return status code 200'
        self.assertEqual(20, self.resp.status_code)

    def test_homepage(self):
        'Homepage must use "index.html" template'
        self.assertTemplateUsed(self.resp, 'index.html')

