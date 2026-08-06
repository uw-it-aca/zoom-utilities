# Copyright 2026 UWIT, University of Washington
# SPDX-License-Identifier: Apache-2.0


import re

from django.test import TestCase

from zoom_utilities.templatetags.vite import vite_scripts, vite_styles


class ViteTestClass(TestCase):
    def test_vite_styles(self):
        entries = ("zoom_utilities_vue/main.js",)
        link = vite_styles(*entries)
        pattern = re.compile(
            '<link rel="stylesheet" href="/static/zoom_utilities/assets/'
            'main[\\d\\w-]*.css" />'
        )
        self.assertTrue(pattern.match(link))

    def test_vite_scripts(self):
        entries = ("zoom_utilities_vue/main.js",)
        script = vite_scripts(*entries)
        pattern = re.compile(
            '<script type="module" src="/static/zoom_utilities/assets/'
            'main[\\d\\w-]*.js"></script>'
        )
        self.assertTrue(pattern.match(script))
