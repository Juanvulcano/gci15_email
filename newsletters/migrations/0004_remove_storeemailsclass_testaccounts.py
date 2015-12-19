# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0003_storeemailsclass_testaccounts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeemailsclass',
            name='testaccounts',
        ),
    ]
