# Copyright 2026 UWIT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response({"context_data": context})

    def get_context_data(self, **kwargs):
        context = {}
        context["signout_url"] = reverse("saml_logout")
        context["debug_mode"] = settings.DEBUG
        return context


class EpicUsageView(HomeView):
    template_name = "epic_usage.html"
