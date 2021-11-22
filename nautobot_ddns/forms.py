import logging

from django import forms

from nautobot_ddns.models import ExtraDNSName
from nautobot.utilities.forms import BootstrapMixin

logger = logging.getLogger('nautobot_ddns')

class ExtraDNSNameEditForm(BootstrapMixin, forms.ModelForm):
    logger.error("Fuck You 1!")
    class Meta:
        model = ExtraDNSName
        fields = ['name']