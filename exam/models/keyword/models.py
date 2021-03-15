"""
*************************************************
© YYYY - 2021 Exam. All Rights Reserved.
*************************************************

keyword.models
"""
import uuid
# django
from django.db import models

# managers
from .managers.keyword_manager import KeywordManager

class Keyword(models.Model):
    """
    Keyword model
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    country_code = models.IntegerField(null=False, blank=False, default=1)
    national_number = models.BigIntegerField()
    location = models.CharField(max_length=255, null=True, blank=True)

    objects = KeywordManager()

    class Meta:
        """
        model meta options
        """
        db_table = 'app_keyword'
