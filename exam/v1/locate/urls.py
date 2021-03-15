"""
*************************************************
© YYYY - 2021 Exam. All Rights Reserved.
*************************************************

auth_user.urls
"""

from django.conf.urls import url
from .views import locate_view

urlpatterns = [
    url(r'^locate_number/?$', locate_view.LocateView.as_view()),
]
