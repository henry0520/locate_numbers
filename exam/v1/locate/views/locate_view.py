"""
********************************************************

© YYYY - 2021 Exam. All Rights Reserved.

********************************************************

API views.locate_view
"""
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from ..serializers.locate_serializers import LocateSerializer
from ..services.locate_services import LocateService, UploadService
from exam.libs.api.base import BaseAPIView

class LocateView(BaseAPIView):
    """
    Locate View
    """
    permission_classes = []
    serializer_class = LocateSerializer
    services_get = LocateService
    services_post = UploadService
    parser_classes = (MultiPartParser, FormParser)

    http_method_names = ['get', 'post',]

    @swagger_auto_schema(tags=['locate'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(tags=['locate'])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
