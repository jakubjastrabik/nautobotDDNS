from django.db import migrations


# noinspection PyUnusedLocal
def add_trailing_dots(apps, schema_editor):
    update_trailing_dots(apps, trailing_dot='.')


# noinspection PyUnusedLocal
def remove_trailing_dots(apps, schema_editor):
    update_trailing_dots(apps, trailing_dot='')


def update_trailing_dots(apps, trailing_dot):
    server_model = apps.get_model('nautobot_ddns', 'Server')
    zone_model = apps.get_model('nautobot_ddns', 'Zone')
    reverse_zone_model = apps.get_model('nautobot_ddns', 'ReverseZone')

    for server in server_model.objects.all():
        server.tsig_key_name = server.tsig_key_name.rstrip('.') + trailing_dot
        server.save()

    for zone in zone_model.objects.all():
        zone.name = zone.name.rstrip('.') + trailing_dot
        zone.save()

    for reverse_zone in reverse_zone_model.objects.all():
        reverse_zone.name = reverse_zone.name.rstrip('.') + trailing_dot
        reverse_zone.save()


class Migration(migrations.Migration):
    dependencies = [
        ('nautobot_ddns', '0003_dnsstatus'),
    ]

    operations = [
        migrations.RunPython(
            code=add_trailing_dots,
            reverse_code=remove_trailing_dots),
    ]