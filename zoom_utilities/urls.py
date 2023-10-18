# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.urls import re_path
from django.views.generic import TemplateView
from zoom_utilities.views.pages import HomeView, EpicUsageView
from zoom_utilities.views.api import ImageAPI


# start with an empty url array
urlpatterns = []

# add debug routes for developing error pages
if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^500$",
            TemplateView.as_view(template_name="500.html"),
            name="500_response",
        ),
        re_path(
            r"^404$",
            TemplateView.as_view(template_name="404.html"),
            name="404_response",
        ),
    ]

urlpatterns += [
    # add api endpoints here
    re_path(r"^api/v1/image/(?P<filename>[\w]+)", ImageAPI.as_view(),
            name="image_api"),
    re_path(r"^epic_usage", EpicUsageView.as_view()),
    re_path(r"^$", HomeView.as_view(), name="index"),
]
