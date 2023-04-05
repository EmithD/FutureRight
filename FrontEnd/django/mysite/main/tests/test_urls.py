from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .. import views


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.index)

    def test_about_us_url_resolves(self):
        url = reverse('about_us')
        self.assertEqual(resolve(url).func, views.about_us)

    def test_help_url_resolves(self):
        url = reverse('help')
        self.assertEqual(resolve(url).func, views.help)

    def test_start_test_url_resolves(self):
        url = reverse('start_test')
        self.assertEqual(resolve(url).func, views.start_test)

    def test_review_test_url_resolves(self):
        url = reverse('review_test')
        self.assertEqual(resolve(url).func, views.review_test)

    def test_test_url_resolves(self):
        url = reverse('test')
        self.assertEqual(resolve(url).func, views.test)

    def test_therm_use_url_resolves(self):
        url = reverse('therm_use')
        self.assertEqual(resolve(url).func, views.therm_use)
