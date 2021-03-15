"""
********************************************************

© YYYY - 2021 Exam. All Rights Reserved.

********************************************************

Task upload notification

"""
import csv
import phonenumbers
from phonenumbers import timezone
from exam import logger
from ..decorators import task
from models.locate.models import Location, Number

LOG = logger.get_logger(__name__)

@task
def uploaded(file_location, **kwargs):
    """
    uploaded
    """
    LOG.info('Open file: %s', file_location)
    with open(file_location, 'r') as reader:
        csv_read = csv.reader(reader)
        x = 0
        for row in csv_read:
            if x!=0:
                us_number = phonenumbers.parse("".join(row), "US")
                for i in timezone.time_zones_for_number(us_number):
                    location, _ = Location.objects.get_or_create(name=i)
                x=+1
            x=+1
    LOG.info('Location added...')

    LOG.info('Uploading number to Number table...')
    with open(file_location, 'r') as reader:
        csv_read = csv.reader(reader)
        x = 0
        for row in csv_read:
            if x!=0:
                us_number = phonenumbers.parse("".join(row), "US")
                location = ', '.join(timezone.time_zones_for_number(us_number))
                validated = True if location!='Etc/Unknown' else False
                data, _ = Number.objects.get_or_create(
                    national_number=us_number.national_number, validated= validated)
                loc = list(timezone.time_zones_for_number(us_number))
                for lrow in Location.objects.filter(name__in=loc):
                    if data.location.filter(name=lrow).count() == 0:
                        data.location.add(lrow)
                        data.save()
                x=+1
            x=+1
    LOG.info('Numbers uploaded...')
