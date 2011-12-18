import json
import re
from datetime import datetime
from urllib import urlencode
from urllib2 import urlopen

from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


GEOCODE_BASE_URL = 'http://maps.googleapis.com/maps/api/geocode/json'


class BasicQueryForm(forms.Form):
    position = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder':'Position'}))
    main_categories = forms.MultipleChoiceField(
        choices=[], widget=forms.CheckboxSelectMultiple(), required=False)

    def __init__(self, user, *args, **kwargs):
        super(BasicQueryForm, self).__init__(*args, **kwargs)

        # TODO - Generalize this request on the utils.py file
        request_data = {
            'oauth_token': json.loads(
                user.social_auth.values()[0]['extra_data'])['access_token'],
            'v': datetime.now().strftime("%Y%m%d"),
        }
        url = '%s/venues/categories?%s' % (
            settings.BASE_FOURSQUARE_URL, urlencode(request_data))
        categories = [
            (x['id'], x['name']) for x in
            json.loads(urlopen(url).readlines()[0])['response']['categories']]
        self.fields['main_categories'].choices = categories

    def clean(self):
        isdigit = lambda x: re.search('^-?\d+((\.|,)\d+)?$', x)
        cleaned_data = self.cleaned_data
        ll = cleaned_data['position'].replace(' ', '').split(',')

        if len(ll) != 2 or not isdigit(ll[0]) or not isdigit(ll[1]):
            geocode_data = {
                'sensor':u'false',
                'address': cleaned_data['position'],
            }
            url = u'%s?%s' % (
                GEOCODE_BASE_URL,
                urlencode(dict([k, v.encode('utf-8')]
                               for k, v in geocode_data.items())))
            raw_response = ''.join(urlopen(url).readlines())
            data = json.loads(raw_response)
            if data["status"] == "OK":
                location = data['results'][0]["geometry"]["location"]
                cleaned_data['position'] = '%s,%s' % (location['lat'],
                                                      location['lng'])
            else:
                raise forms.ValidationError(
                    _('The given position value is not valid'))
        return cleaned_data
