# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0002_auto_20151218_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeemailsclass',
            name='testaccounts',
            field=models.CharField(default=' ', unique=True, max_length=120),
            preserve_default=False,
        ),
    ]
