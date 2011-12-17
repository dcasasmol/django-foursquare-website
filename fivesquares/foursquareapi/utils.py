import json
import urllib2
from datetime import datetime
from urllib import urlencode

from django.conf import settings


def get_ordered_venues(ll, categories=None):
    request_data = {
        'll': ll,
        'oauth_token': settings.OAUTH_FOURSQUARE,
        'v': datetime.now().strftime("%Y%m%d"),
    }
    url = '%s/venues/search?%s' % (
        settings.BASE_FOURSQUARE_URL, urlencode(request_data))
    venues = []
    aux = url
    if(categories != None):
        for item in categories:
            url = aux
            url = url + '&limit=15&categoryId=' + item
            venues += get_venues(url)

    else:
        venues += get_venues(url)
    return sorted(venues, key=lambda venues: venues['distance'])


def get_venues(url):
    open = urllib2.urlopen(url)
    line = open.readlines()[0]
    data = json.loads(line)

    venues = []
    for item in data['response']['venues']:
        address = 'address' in item['location'] and item['location']['address'] or ''
        phone = 'phone' in item['contact'] and item['contact']['phone'] or ''
        category = len(item['categories']) > 0 and item['categories'][0]['name'] or ''
        venue = {'name': item['name'],
                 'category': category,
                 'address': address,
                 'phone': phone,
                 'distance': item['location']['distance'],
                 'checkins': item['stats']['checkinsCount'],
                 'users': item['stats']['usersCount']}
        venues.append(venue)

    return venues
