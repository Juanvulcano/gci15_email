# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0006_auto_20151218_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='addemail',
            name='email',
            field=models.EmailField(default=' ', unique=True, max_length=254),
            preserve_default=False,
        ),
    ]
