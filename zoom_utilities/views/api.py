# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, StreamingHttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from zoom_utilities.dao.file import read_file
from datetime import datetime, timedelta


@method_decorator(login_required, name='dispatch')
class ImageAPI(View):
    cache_time = 60 * 60 * 4
    date_format = '%a, %d %b %Y %H:%M:%S GMT'

    def get(self, request, *args, **kwargs):
        filename = kwargs.get('filename')
        now = datetime.utcnow()
        expires = now + timedelta(seconds=self.cache_time)
        try:
            response = StreamingHttpResponse(read_file(filename),
                                             content_type='image/jpeg')
            response['Cache-Control'] = 'public,max-age={}'.format(
                self.cache_time)
            response['Expires'] = expires.strftime(self.date_format)
            response['Last-Modified'] = now.strftime(self.date_format)
            return response
        except ObjectDoesNotExist:
            status = 304 if ('HTTP_IF_MODIFIED_SINCE' in request.META) else 404
            return HttpResponse(status=status)
