"""
*************************************************
© YYYY - 2021 Exam. All Rights Reserved.
*************************************************

API libs.templates.helpers
"""
from django.conf import settings
from django_jinja import library
from django.template.defaultfilters import date

SUBJECT_TITLE = 'Philippine ID - '

@library.filter
def dttime_format(val):
    """
    filter to format datetime based on settings DATETIME_FORMAT
    """
    return date(val, settings.DATETIME_FORMAT)
