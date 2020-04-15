import time
from django.conf import settings

class TimeDelayMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        self.delay = 0.5


    def __call__(self, request):
        if '/estoque' in request.path:
            time.sleep(self.delay)
        response = self.get_response(request)
        return response
