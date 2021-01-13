from django import forms
from ..models.tnb_faucet import FaucetOption

FAUCET_OPTIONS = (
    (100, '100 coins / 3 hrs'),
    (500, '500 coins / 1 day'),
    (1500, '1500 coins / 3 days'),
)

class FaucetForm(forms.Form):
    url = forms.URLField(required=True, widget= forms.TextInput
                           (attrs={'placeholder':'URL of a facebook post or tweet containing your thenewboston address...'}))
    amount = forms.ModelChoiceField(queryset=FaucetOption.objects.all(), initial=FaucetOption.objects.first())