import urllib2
import json


def get_ordered_venues(url):
    return order_data(get_venues(url))


def get_venues(url):
    open = urllib2.urlopen(url)
    line = open.readlines()[0]
    data = json.loads(line)

    venues = []
    for item in data['response']['venues']:
        address = 'address' in item['location'] and item['location']['address'] or ''
        phone = 'phone' in item['contact'] and item['contact']['phone'] or ''
        venue = {'name': item['name'],
                 'category': item['categories'][0]['name'],
                 'address': address,
                 'phone': phone,
                 'distance': item['location']['distance'],
                 'checkins': item['stats']['checkinsCount'],
                 'users': item['stats']['usersCount']}
        venues.append(venue)

    return venues


def order_data(elements):
    return sorted(elements, key=lambda item: item['distance'])
