# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='AuthorID',
            field=models.ForeignKey(related_name='books', to='app1.Author'),
        ),
    ]
