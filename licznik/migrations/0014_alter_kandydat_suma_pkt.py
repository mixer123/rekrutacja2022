# Generated by Django 3.2.5 on 2022-01-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licznik', '0013_auto_20220111_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandydat',
            name='suma_pkt',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=5),
        ),
    ]
