from django.test import TestCase
from . import models
from datetime import datetime


class MyTests(TestCase):
    def test_time(self):
        now = datetime.now().timestamp()
        self.assertLess(abs(now - models.get_current_time()), 2)