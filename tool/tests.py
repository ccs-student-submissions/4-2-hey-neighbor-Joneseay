from django.test import TestCase
from django.urls import reverse


class HomePageViewTest(TestCase):


    def test_view_url_exist_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
