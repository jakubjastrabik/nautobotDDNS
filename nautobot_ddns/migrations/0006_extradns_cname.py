from django.db import migrations


class Migration(migrations.Migration):
    operations = [
        migrations.RemoveField(
            model_name='extradnsname',
            name='reverse_action',
        ),
        migrations.RemoveField(
            model_name='extradnsname',
            name='reverse_rcode',
        ),
    ]