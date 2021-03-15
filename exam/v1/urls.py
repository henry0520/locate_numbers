"""
*************************************************
© YYYY - 2021 Exam. All Rights Reserved.
*************************************************

v1.urls endpoint
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('v1.auth_user.urls')),
    url(r'^', include('v1.locate.urls'))
]
