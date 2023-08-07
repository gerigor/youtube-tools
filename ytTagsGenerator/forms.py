from django import forms
import re


class TagsGeneratorForm(forms.Form):
    url = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Video url', 'class': 'form-control'}),
        label=False,
        required=True,
    )

    def clean_url(self):
        data = self.cleaned_data['url']
        regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
        if not re.match(regex, data):
            raise forms.ValidationError('Enter correct url.')
        return data
