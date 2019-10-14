from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg_webapp', '0002_reportsettings_info_blocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportsettings',
            name='language',
            field=models.CharField(default='en', max_length=2),
        ),
    ]