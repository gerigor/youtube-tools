from django import forms


class TagsGeneratorForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Video title', 'class': 'form-control'}),
        label=False,
        required=True,
        max_length=64,
    )

