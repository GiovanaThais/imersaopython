# Generated by Django 3.2.5 on 2021-07-27 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0013_alter_pedido_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 27, 17, 39, 42, 247919), verbose_name='data'),
        ),
    ]