# Create your views here.
from datetime import datetime
from urllib import urlencode

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from foursquareapi.forms import BasicQueryForm
from foursquareapi.utils import get_ordered_venues


def home(request):
    venues = []
    if request.method == 'POST':
        form = BasicQueryForm(request.POST)
        venues = get_ordered_venues(form.data['position'])
    else:
        form = BasicQueryForm()

    return render_to_response(
        'foursquareapi/index.html', {
            'form': form, 'venues': venues,
        },
        context_instance=RequestContext(request))
