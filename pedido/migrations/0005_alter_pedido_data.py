# Generated by Django 3.2.5 on 2021-07-25 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_auto_20210724_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 25, 18, 10, 16, 266864), verbose_name='data'),
        ),
    ]