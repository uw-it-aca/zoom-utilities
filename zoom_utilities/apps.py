# Copyright 2026 UWIT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.apps import AppConfig
from django.contrib.staticfiles.apps import StaticFilesConfig


class ZoomUtilitiesFilesConfig(StaticFilesConfig):
    ignore_patterns = ["CVS", "*~"]


class ZoomUtilitiesConfig(AppConfig):
    name = "zoom_utilities"
