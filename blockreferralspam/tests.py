from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class BlockreferralspamTestCase(TestCase):

    def test_get_200(self):
        # index view
        c = Client()
        index_url = reverse('index')
        index_res = c.get(index_url)
        self.assertEqual(index_res.status_code, 200)

    def test_get_404(self):
        # index view
        c = Client(HTTP_REFERER='site5.floating-share-buttons.com')
        index_url = reverse('index')
        index_res = c.get(index_url)
        self.assertEqual(index_res.status_code, 404)

        c = Client(HTTP_REFERER='floating-share-buttons.com')
        index_url = reverse('index')
        index_res = c.get(index_url)
        self.assertEqual(index_res.status_code, 404)
