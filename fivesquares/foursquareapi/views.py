# Create your views here.

from datetime import datetime
from urllib import urlencode

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from foursquareapi.forms import BasicQueryForm
from foursquareapi.utils import get_ordered_data


def home(request):
    venues = []
    if request.method == 'POST':
        form = BasicQueryForm(request.POST)
        request_data = {
            'oauth_token': settings.OAUTH_FOURSQUARE,
            'll': form.data['position'],
            'v': datetime.now().strftime("%Y%m%d"),
        }
        url = '%s/venues/search?%s' % (
            settings.BASE_FOURSQUARE_URL, urlencode(request_data))
        venues = get_ordered_data(url)
    else:
        form = BasicQueryForm()

    return render_to_response(
        'foursquareapi/index.html', {
            'form': form, 'venues': venues,
        },
        context_instance=RequestContext(request))
