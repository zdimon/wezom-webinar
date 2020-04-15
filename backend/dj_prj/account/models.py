from django.db import models

from django.contrib.auth.models import User

class UserProfile(User):
    GENDER = (
        ('male', 'Man'),
        ('female','Woman')
    )

    gender = models.CharField(
        verbose_name='Gender',
        choices=GENDER,
        db_index=True,
        default='male',
        max_length=6)

    firstname = models.CharField(default='', max_length=250)
    lastname = models.CharField(default='', max_length=250)
