"""
********************************************************

© YYYY - 2021. All Rights Reserved.

********************************************************

management command module

"""
import csv
# core
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from models.locate.models import Number

# logger
from exam import logger

LOG = logger.get_logger(__name__)

class Command(BaseCommand):
    """
    Command
    """
    def handle(self, **options):
        """
        Handle
        self (object)
        options (dictionary)
        """
        file_location = '{0}/{1}'.format(settings.BASE_DIR, 'output.csv')
        LOG.info('Writing file to %s' % file_location)
        with open(file_location, mode='w') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['numbers','valid','location'])
            for row in Number.objects.all():
                writer.writerow(['%s' % row.numbers, '%s' % row.validated, '%s' % row.city])
            f.close()
        LOG.info('The output.csv is created and located to %s' % file_location)
