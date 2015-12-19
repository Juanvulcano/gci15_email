# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0007_addemail_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addemail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
