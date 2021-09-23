# Generated by Django 3.2.7 on 2021-09-21 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='address',
            field=models.CharField(blank=True, max_length=95),
        ),
        migrations.AlterField(
            model_name='loja',
            name='categories',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='loja',
            name='city',
            field=models.CharField(blank=True, max_length=189),
        ),
        migrations.AlterField(
            model_name='loja',
            name='country',
            field=models.CharField(blank=True, max_length=56),
        ),
        migrations.AlterField(
            model_name='loja',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='loja',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='loja',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='loja',
            name='postalCode',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='loja',
            name='province',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='loja',
            name='websites',
            field=models.CharField(blank=True, max_length=2083),
        ),
    ]
