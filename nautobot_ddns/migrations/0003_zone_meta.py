from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('nautobot_ddns', '0002_ensure_trailing_dot'),
    ]
    
    operations = [
        migrations.AlterModelOptions(
            name='zone',
            options={'ordering': ('name',), 'verbose_name': 'forward zone', 'verbose_name_plural': 'forward zones'},
        ),
    ]