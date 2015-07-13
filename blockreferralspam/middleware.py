import re
import os
from django.http import HttpResponse, Http404


class KillSpam:

    def process_request(self, request):
        if 'HTTP_REFERER' in request.META:
            f = open(
                os.path.dirname(os.path.realpath(__file__)) + '/spammers.txt', 'r')
            for line in f.readlines():
                my_regex = r".*" + re.escape(line.rstrip()) + r".*"
                if re.search(my_regex, request.META['HTTP_REFERER'], re.IGNORECASE):
                    raise Http404
