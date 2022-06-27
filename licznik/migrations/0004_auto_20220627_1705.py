# Generated by Django 3.2.5 on 2022-06-27 17:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licznik', '0003_auto_20220627_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandydat',
            name='biol_oc',
            field=models.ForeignKey(default='default_ocena', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='biol_oc', to='licznik.ocena', verbose_name='Biologia ocena'),
        ),
        migrations.AlterField(
            model_name='kandydat',
            name='inf_oc',
            field=models.ForeignKey(default='default_ocena', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inf_oc', to='licznik.ocena', verbose_name='Informatyka ocena'),
        ),
        migrations.AlterField(
            model_name='kandydat',
            name='j_obcy_egz',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='J.obcy punkty egzamin'),
        ),
        migrations.AlterField(
            model_name='kandydat',
            name='j_pol_egz',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='J.polski punkty egzamin'),
        ),
        migrations.AlterField(
            model_name='kandydat',
            name='j_pol_oc',
            field=models.ForeignKey(default='default_ocena', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='j_pol_oc', to='licznik.ocena', verbose_name='J.polski ocena'),
        ),
        migrations.AlterField(
            model_name='kandydat',
            name='mat_egz',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Matematyka punkty egzamin'),
        ),
        migrations.AlterField(
            model_name='kandydat',
            name='mat_oc',
            field=models.ForeignKey(default='default_ocena', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mat_oc', to='licznik.ocena', verbose_name='Matematyka ocena'),
        ),
    ]