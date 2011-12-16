from django import forms
from django.utils.translation import ugettext_lazy as _


class BasicQueryForm(forms.Form):
    position = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        ll = cleaned_data['position'].replace(' ', '').split(',')

        if len(ll) != 2 or not ll[0].isdigit() or not ll[1].isdigit():
            raise forms.ValidationError(
                _('The given position value is not valid'))
        return cleaned_data
