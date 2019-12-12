from django.test import TestCase

from . import models


class TestModelAccess(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        models.Book.objects.get_or_create(name="Alice in Wonderland")

    def test_get_or_create_book(self):
        models.Book.objects.get_or_create(name="Alice in Wonderland")
