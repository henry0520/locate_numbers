"""
*************************************************
© YYYY - 2021 Exam. All Rights Reserved.
*************************************************

keyword.managers.user_manager
"""
import phonenumbers
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import BaseUserManager

from exam import logger

LOG = logger.get_logger(__name__)

class UserQueryset(models.query.QuerySet):
    """
    User queryset
    """
    def find_by_uuid(self, uuid):
        """
        find by email
        """
        try:
            return self.get(uuid=uuid)
        except (self.model.DoesNotExist, ValidationError):
            return None

    def find_by_number(self, number):
        """
        find by number
        """
        us_number = phonenumbers.parse(number, "US")
        try:
            return self.get(national_number=us_number.national_number)
        except (self.model.DoesNotExist, ValidationError):
            return None

class KeywordManager(BaseUserManager):
    """
    keyword manager
    """
    def get_queryset(self):
        """
        get queryset
        """
        return UserQueryset(self.model, using=self._db)

    def find_by_uuid(self, uuid):
        """
        find by uuid
        """
        return self.get_queryset().find_by_uuid(uuid)

    def find_by_number(self, number):
        """
        find by number
        """
        return self.get_queryset().find_by_number(number)
