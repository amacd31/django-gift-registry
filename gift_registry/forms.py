from django import forms

from gift_registry.models import Giver

class GiverForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = Giver
        fields = '__all__'

        widgets = {
            'gift': forms.HiddenInput,
        }
