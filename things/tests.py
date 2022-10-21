from django.test import TestCase

# Create your tests here.
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Thing

class ThingModelTestCase(TestCase):

    def setUp(self):
        self.thing1 = Thing.objects.create(
        name='thingname',
        description='',
        quantity=10,
        )

    def test_valid_user(self):
        self.assert_user_is_valid()

    def assert_user_is_valid(self):
        try:
            self.thing1.full_clean()
        except(ValidationError):
            self.fail('Test user shoukd be valid')

    def assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing1.full_clean()
