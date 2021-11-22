from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nautobot_ddns', '0005_extradnsname'),
    ]

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