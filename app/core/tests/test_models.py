from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfully(self):
        """ Test creating a new user with an email is successfull """
        email = 'test@mohyddin.com'
        password = '12345678'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalized_user_email(self):

        email = 'test@DOMAIN.COM'

        user = get_user_model().objects.create_user(email=email,
                                                    password='123456!@#$')

        self.assertEquals(user.email, email.lower())

    def test_user_no_email(self):
        """Test creating a user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1223@#$')

    def test_create_superuser(self):
        """Tests create user is super user"""
        email = 'admin@test.com'
        password = '12345$#$'

        user = get_user_model().objects.create_superuser(email=email,
                                                         password=password)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
