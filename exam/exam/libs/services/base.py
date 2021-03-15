"""
********************************************************

© YYYY - 2021 Exam. All Rights Reserved.

********************************************************

API exam.libs.services.base

Author: Henry J. Medina
"""
from exam import logger
LOG = logger.get_logger(__name__)

class BaseService:
    """
    Base login service
    """
    def __init__(self, **kwargs):
        """
        initialization
        """
        #data
        self.data = kwargs.get('data', {})

        # context
        self.context = kwargs.get('context', {})

        # request
        self.request = kwargs.get('request', None)

        self.data = self._request_data()

        # uuid
        self.uuid = kwargs.get('uuid', None)

        # serializers
        self.serializer = None

        # many
        self.many = True

        # errors
        self.errors = {}

        # instance
        self.instance = None

    def _request_data(self):
        """
        Private request data
        """
        return self.request.data if self.request else {}

    def get_queryset(self):
        """
        abstract method, required derived classes to override
        """
        self.errors = {'not_implemented': 'Not Implemented'}
        raise NotImplementedError

    def run(self):
        """
        Run service

        Parameter: self (object)
        Return: (object) instance
        """
        serializer = self.serializer(
            self.get_queryset(),
            many=self.many,
            context={'request': self.request}
        )
        return serializer.data
