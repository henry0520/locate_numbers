"""
********************************************************

© YYYY - 2021 Exam. All Rights Reserved.

********************************************************

API services.locate_services
"""
import csv
import phonenumbers
from phonenumbers import timezone

# django
from django.conf import settings

# libs
from exam.libs.services.base import BaseService

# utils
from exam.utils.handler.exception import InvalidInput

# models
from models.locate.models import Number, Location
from models.keyword.models import Keyword

# serializers
from ..serializers.locate_serializers import LocateSerializer, UploadSerializer

# tasks
from tasks.upload import number as number_notification

from exam import logger

LOG = logger.get_logger(__name__)

class LocateService(BaseService):
    """
    Locate service
    """

    def get_timezone_for_number(self):
        """
        get timezone for number
        """
        us_number = phonenumbers.parse(self.request.GET['number'], "US")
        return list(timezone.time_zones_for_number(us_number))

    def get_location(self):
        """
        get location
        """
        if not self.request.GET.get('number', None):
            self.errors = {'number': 'Missing number parameter'}
            raise InvalidInput
        keyword = Keyword.objects.find_by_number(self.request.GET['number'])
        if not keyword:
            return self.get_timezone_for_number()

        return [keyword.location]

    def get_queryset(self):
        """
        get queryset
        """
        location = self.get_location()
        return Number.objects.filter_by_location(location)

    def run(self):
        """
        run service
        """
        self.serializer = LocateSerializer
        serializer = self.serializer(
            self.get_queryset(),
            many=self.many,
            context={'request': self.request},
        )
        self.instance = serializer.instance
        return serializer.data

class UploadService(BaseService):
    """
    upload service
    """

    def handle_uploaded_file(self, uploaded_file):
        """
        Handle uploaded file

        Parameter: self(object)
        Return (NoneType) None
        """
        self.name = '{0}'.format(self.data['file'].name)

        file_destination = '{0}{1}'.format(settings.CSV_UPLOAD_DIR, self.name)
        with open(file_destination, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
            destination.close()

    def _open_file(self):
        """
        private open file
        """
        return '{0}{1}'.format(settings.CSV_UPLOAD_DIR, self.name)

    def run(self):
        """
        run service
        """
        self.serializer = UploadSerializer
        serializer = self.serializer(data=self.request.data)
        if not serializer.is_valid():
            self.errors = serializer.errors
            raise InvalidInput
        self.handle_uploaded_file(serializer.validated_data['file'])
        number_notification.uploaded.apply_async([self._open_file()])
        return {'message': 'Upload sent to task...'}
