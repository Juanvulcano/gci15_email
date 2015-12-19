# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0005_addemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeemailsclass',
            name='accounts',
            field=models.ForeignKey(to='newsletters.AddEmail'),
        ),
    ]
