# Generated by Django 3.2.5 on 2021-07-23 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adicional',
            options={'verbose_name': 'Adicional', 'verbose_name_plural': 'Adicionais'},
        ),
        migrations.AlterModelOptions(
            name='opcoes',
            options={'verbose_name': 'Opcoes', 'verbose_name_plural': 'Opcoes'},
        ),
    ]
