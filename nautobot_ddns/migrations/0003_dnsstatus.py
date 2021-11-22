from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0036_standardize_description'),
        ('nautobot_ddns', '0002_add_ttl'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNSStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('forward_action', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('forward_rcode', models.PositiveIntegerField(blank=True, null=True)),
                ('reverse_action', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('reverse_rcode', models.PositiveIntegerField(blank=True, null=True)),
                ('ip_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ipam.ipaddress')),
            ],
            options={
                'verbose_name': 'DNS status',
                'verbose_name_plural': 'DNS status',
            },
        ),
    ]