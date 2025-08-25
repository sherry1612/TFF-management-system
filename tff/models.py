from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    department = models.CharField(
        max_length=50,
        choices=[
            ('Administration', 'Administration'),
            ('Procurement', 'Procurement'),
            ('Finance', 'Finance'),
            ('HR', 'HR'),
            ('ICT', 'ICT'),
        ]
    )
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
