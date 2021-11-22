import logging

from django import forms

from nautobot_ddns.models import ExtraDNSName
from nautobot.utilities.forms import BootstrapMixin

logger = logging.getLogger('nautobot_ddns')

class ExtraDNSNameEditForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = ExtraDNSName
        fields = ['name']