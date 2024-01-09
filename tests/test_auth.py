from unittest import TestCase


class TestAuthenticationFunction(TestCase):
    """Test authentication Function"""

    def test_dummy(self):
        """Test Dummy Authentication"""
        self.assertEqual("foo".upper(), "FOO")
