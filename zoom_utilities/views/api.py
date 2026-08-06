# Copyright 2026 UWIT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.http import FileResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(login_required, name='dispatch')
class ImageAPI(View):
    cache_time = 60 * 60 * 4
    date_format = '%a, %d %b %Y %H:%M:%S GMT'

    def get(self, request, *args, **kwargs):
        filename = kwargs.get('filename')
        try:
            response = FileResponse(default_storage.open(filename, mode='rb'),
                                    content_type='image/jpeg')
            now = datetime.now(datetime.UTC)
            expires = now + timedelta(seconds=self.cache_time)
            response['Cache-Control'] = f'public,max-age={self.cache_time}'
            response['Expires'] = expires.strftime(self.date_format)
            response['Last-Modified'] = now.strftime(self.date_format)
            return response
        except FileNotFoundError:
            status = 304 if ('HTTP_IF_MODIFIED_SINCE' in request.META) else 404
            return HttpResponse(status=status)
