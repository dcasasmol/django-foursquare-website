# Create your views here.
import json
from datetime import datetime
from urllib import urlencode

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from foursquareapi.forms import BasicQueryForm
from foursquareapi.utils import get_ordered_venues


@login_required
def home(request):
    return render_to_response(
        'foursquareapi/index.html', {},
        context_instance=RequestContext(request))


@login_required
def query(request):
    venues = []
    if request.method == 'POST':
        form = BasicQueryForm(request.POST)
        if form.is_valid():
            venues = get_ordered_venues(
                form.data['position'],
                user_oauth=json.loads(
                    request.user.social_auth.values()[0]['extra_data'])[
                        'access_token'])
    else:
        form = BasicQueryForm()

    return render_to_response(
        'foursquareapi/query.html', {
            'form': form, 'venues': venues,
        },
        context_instance=RequestContext(request))
