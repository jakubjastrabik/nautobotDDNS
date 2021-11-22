from django.db import migrations


class Migration(migrations.Migration):
    operations = [
        migrations.AlterModelOptions(
            name='zone',
            options={'ordering': ('name',), 'verbose_name': 'forward zone', 'verbose_name_plural': 'forward zones'},
        ),
    ]