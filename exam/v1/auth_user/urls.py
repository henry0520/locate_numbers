"""
*************************************************
© YYYY - 2021 Exam. All Rights Reserved.
*************************************************

auth_user.urls
"""

from django.conf.urls import url
from .views import login_view

urlpatterns = [
    url(r'^api/v1/accounts/login/?$', login_view.LoginView.as_view()),
]

