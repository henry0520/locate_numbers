"""
*************************************************
© YYYY - 2021 Exam. All Rights Reserved.
*************************************************

upload.models
"""
import uuid
import phonenumbers
from phonenumbers import timezone

# django
from django.db import models

# managers
from .managers.upload_manager import UploadManager

class Location(models.Model):
    """
    Location model
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        """
        model meta options
        """
        db_table = 'app_location'

class Number(models.Model):
    """
    Number model
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    country_code = models.IntegerField(null=False, blank=False, default=1)
    national_number = models.BigIntegerField()
    validated = models.BooleanField(default=False)
    location = models.ManyToManyField('Location', related_name='number_location')

    objects = UploadManager()

    class Meta:
        """
        model meta options
        """
        db_table = 'app_number'
        unique_together = ('country_code', 'national_number',)

    @property
    def city(self):
        """
        city
        """
        city = ", ".join([row.name for row in self.location.all()])
        return 'n/a' if city == 'Etc/Unknown' else city

    @property
    def numbers(self):
        """
        numbers
        """
        us_number = phonenumbers.parse('%s' % self.national_number, 'US')
        return phonenumbers.format_number(us_number, phonenumbers.PhoneNumberFormat.NATIONAL)
