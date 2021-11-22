from django.db import migrations, models
import django.db.models.deletion
import nautobot_ddns.validators


class Migration(migrations.Migration):
    operations = [
         migrations.CreateModel(
            name='ExtraDNSName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, validators=[nautobot_ddns.validators.HostnameValidator()])),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('forward_action', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('forward_rcode', models.PositiveIntegerField(blank=True, null=True)),
                ('reverse_action', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('reverse_rcode', models.PositiveIntegerField(blank=True, null=True)),
                ('ip_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipam.ipaddress')),
            ],
            options={
                'verbose_name': 'extra DNS name',
                'verbose_name_plural': 'extra DNS names',
                'unique_together': {('ip_address', 'name')},
            },
        ),
    ]