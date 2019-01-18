from django.test import TestCase
# Create your tests here.

class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url = reversed('home')

