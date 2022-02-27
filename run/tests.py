from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

class RunTest(SimpleTestCase):
  def test_home_page_status_code(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_about_page_status_code(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_info_page_status_code(self):
    url = reverse('info')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
  
  def test_club_page_status_code(self):
    url = reverse('club')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    
  def test_home_base_template(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'home.html')
    self.assertTemplateUsed(response, 'base.html')


# Create your tests here.
