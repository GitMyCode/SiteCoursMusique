import datetime

from django.utils import timezone
from django.test import TestCase

from news.models import New

class NewMethodTests(TestCase):

    def test_was_published_recently_with_future_new(self):
        """
        was_published_recently() should return False for news whose
        creation_date is in the future
        """
        future_new = New(creation_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_new.was_published_recently(), False)


    def test_was_published_recently_with_old_new(self):
        """
        was_published_recently() should return False for polls whose creation_date
        is older than 1 day
        """
        old_new = New(creation_date=timezone.now() - datetime.timedelta(days=30))
        self.assertEqual(old_new.was_published_recently(), False)


    def test_was_published_recently_with_recent_new(self):
        """
        was_published_recently() should return True for polls whose creation_date
        is within the last day
        """
        recent_new = New(creation_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertEqual(recent_new.was_published_recently(), True)