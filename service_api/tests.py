from django.test import TestCase
from django.shortcuts import reverse, get_object_or_404
from .business_layer.short_url_generator import ShortUrlGenerator
from django.conf import settings
from .models import Url


# Create your tests here.


class IndexViewTest(TestCase):

    def test_view_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_redirect_after_valid_form_submit(self):
        response = self.client.post(reverse('index'), data={'url': 'https://google.com'})
        self.assertEqual(response.status_code, 302)

    def test_short_url_record_after_redirect(self):
        url = 'https://google.com'
        response = self.client.post(reverse('index'), data={'url': url})
        self.assertEqual(response.status_code, 302)
        obj = Url.objects.filter(url=url).first()
        self.assertNotEqual(obj, None)


class ResolveViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        short_url = ShortUrlGenerator(settings.SHORT_URL_LENGTH).generate_short_url()
        Url.objects.create(url='https://google.com', short_url=short_url)

    def test_short_url_resolve(self):
        long_url = 'https://google.com'
        url = Url.objects.filter(url=long_url).first()
        response = self.client.get(reverse('short_url_1', kwargs={'short_url': url.short_url}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, long_url)
