# Generated by Django 3.2.7 on 2021-09-21 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_alter_loja_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='postalCode',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
