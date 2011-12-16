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
    quicksort(elements, 0, len(elements) - 1)
    return elements


def quicksort(elements, left, right):
    if left < right:
        pivot = elements[(left + right) / 2]['distance']
        l, r = left, right
        while l <= r:
            while elements[l]['distance'] < pivot:
                l += 1
            while elements[r]['distance'] > pivot:
                r -= 1
            if l <= r:
                (elements[l]['distance'],
                 elements[r]['distance']) = (
                     elements[r]['distance'],
                     elements[l]['distance'])
                l += 1
                r -= 1
        if left < r:
            quicksort(elements, left, r)
        if l < right:
            quicksort(elements, l, right)
    return elements
