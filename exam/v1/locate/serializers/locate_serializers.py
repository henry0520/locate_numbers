"""
********************************************************

© YYYY - 2021 Exam. All Rights Reserved.

********************************************************

API locate.serializers.locate_serializers
"""
from django.conf import settings
from rest_framework import serializers
from django.core.validators import FileExtensionValidator

class LocateSerializer(serializers.Serializer):
    """
    locate serializer
    """
    location = serializers.SerializerMethodField()
    numbers = serializers.SerializerMethodField()

    def get_location(self, obj):
        """
        get location
        """
        return obj.city

    def get_numbers(self, obj):
        """
        get numbers
        """
        return obj.numbers

    class Meta:
        """
        class meta serializer
        """
        fields = ['uuid', 'numbers', 'valid', 'location',]

class UploadSerializer(serializers.Serializer):
    """
    upload serializer
    """
    file = serializers.FileField(
        required=True,
        error_messages={
            'required': 'File is required',
            'blank': 'File should not be blank',
            'null': 'File should not be null',
        },
        style={'input_type': 'file'},
        validators=[FileExtensionValidator(settings.VALID_CSV_FORMATS),]
    )

    def get_file_size(self, uploaded_file):
        """
        Has valid file size

        Parameter: uploaded file (object)
        Return: (int) size of the uploaded file
        """
        return uploaded_file.file.seek(0, 2)

    def has_valid_file_size(self, size=0):
        """
        Has valid file size

        Parameter: size in bytes (int)
        Return: (boolean)
        """
        if size > settings.CSV_FILE_LIMIT:
            return False

        return True

    def validate_file(self, uploaded_file):
        """
        Validate file
        """
        get_file_size = self.get_file_size(uploaded_file)
        has_valid_file_size = self.has_valid_file_size(get_file_size)
        if not has_valid_file_size:
            raise serializers.ValidationError(
                'File size should not greater than %s bytes' % settings.CSV_FILE_LIMIT)

        return uploaded_file
