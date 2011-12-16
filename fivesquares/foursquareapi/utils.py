import urllib2
import json


def get_ordered_data(url):
    return order_data(get_data(url))


def get_data(url):
    open = urllib2.urlopen(url)
    line = open.readlines()[0]
    data = json.loads(line)
    return data['response']['venues']


def show_data(mylist, indent=1, level=0):
    for item in mylist:
        if isinstance(item, list):
            show_data(item, indent, level + 1)
        else:
            if indent:
                for tab in range(level):
                    print "\t"
            print item


def order_data(elements):
    quicksort(elements, 0, len(elements) - 1)
    return elements


def quicksort(elements, left, right):
    if left < right:
        pivot = elements[(left + right) / 2]['location']['distance']
        l, r = left, right
        while l <= r:
            while elements[l]['location']['distance'] < pivot:
                l += 1
            while elements[r]['location']['distance'] > pivot:
                r -= 1
            if l <= r:
                (elements[l]['location']['distance'],
                 elements[r]['location']['distance']) = (
                     elements[r]['location']['distance'],
                     elements[l]['location']['distance'])
                l += 1
                r -= 1
        if left < r:
            quicksort(elements, left, r)
        if l < right:
            quicksort(elements, l, right)
    return elements
