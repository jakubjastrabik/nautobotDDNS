from django import forms

from nautobotDDNS.models import ExtraDNSName
from nautobot.utilities.forms import BootstrapMixin


class ExtraDNSNameEditForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = ExtraDNSName
        fields = ['name']
