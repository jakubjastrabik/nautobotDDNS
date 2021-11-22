from django.db import migrations, models


class Migration(migrations.Migration):
    operations = [
        migrations.AddField(
            model_name='reversezone',
            name='ttl',
            field=models.PositiveIntegerField(default=3600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zone',
            name='ttl',
            field=models.PositiveIntegerField(default=3600),
            preserve_default=False,
        ),
    ]