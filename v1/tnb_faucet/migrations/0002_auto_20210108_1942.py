# Generated by Django 3.1.3 on 2021-01-08 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tnb_faucet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faucetmodel',
            name='next_valid_access_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 8, 22, 42, 57, 74194)),
        ),
    ]