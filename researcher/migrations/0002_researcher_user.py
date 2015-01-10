# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('researcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
