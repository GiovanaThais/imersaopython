# Generated by Django 3.2.5 on 2021-07-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20210723_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adicional',
            name='nome',
            field=models.CharField(max_length=100, unique=True, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='categoria',
            field=models.CharField(max_length=200, verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='opcoes',
            name='acrecimo',
            field=models.FloatField(default=0, verbose_name='acrescimo'),
        ),
        migrations.AlterField(
            model_name='opcoes',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='opcoes',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='img',
            field=models.ImageField(upload_to='post_img', verbose_name='imagem'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='ingredientes',
            field=models.CharField(max_length=2000, verbose_name='ingredientes'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome_produto',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
    ]
