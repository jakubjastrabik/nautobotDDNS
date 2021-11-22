from django.db import migrations, models
import django.db.models.deletion
import nautobot.ipam.fields
import nautobot_ddns.validators

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ipam', '0004_fixup_p2p_broadcast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('server', models.CharField(max_length=255, validators=[nautobot_ddns.validators.HostnameAddressValidator()])),
                ('tsig_key_name', models.CharField(max_length=255, validators=[nautobot_ddns.validators.HostnameValidator()])),
                ('tsig_algorithm', models.CharField(max_length=32)),
                ('tsig_key', models.CharField(max_length=512, validators=[nautobot_ddns.validators.validate_base64])),
            ],
            options={
                'verbose_name': 'dynamic DNS Server',
                'verbose_name_plural': 'dynamic DNS Servers',
                'ordering': ('server', 'tsig_key_name'),
                'unique_together': {('server', 'tsig_key_name')},
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True, validators=[nautobot_ddns.validators.HostnameValidator()])),
                ('ttl', models.PositiveIntegerField()),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nautobot_ddns.server')),
            ],
            options={
                'verbose_name': 'forward zone',
                'verbose_name_plural': 'forward zones',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ReverseZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('prefix', nautobot.ipam.fields.VarbinaryIPField(unique=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('ttl', models.PositiveIntegerField()),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nautobot_ddns.server')),
            ],
            options={
                'verbose_name': 'reverse zone',
                'verbose_name_plural': 'reverse zones',
                'ordering': ('prefix',),
            },
        ),
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