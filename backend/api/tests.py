from django.test import TestCase
from django.apps import apps
from api.apps import ApiConfig
from .models import UserInput

class YourTestClass(TestCase):
  @classmethod
  def setUpTestData(cls):
    print("setUpTestData: Run once to set up non-modified data for all class methods.")
    UserInput.objects.create(text='test user input')

  def test_text_label(self):
    user_input = UserInput.objects.get(id=1)
    field_label = user_input._meta.get_field('text').verbose_name
    self.assertEquals(field_label, 'text')

  def test_object_returns_text(self):
    user_input = UserInput.objects.get(id=1)
    self.assertEquals(str(user_input), user_input.text)

class ApiConfigTest(TestCase):
  def test_apps(self):
    self.assertEqual(ApiConfig.name, 'api')
    self.assertEqual(apps.get_app_config('api').name, 'api')
 