# Generated by Django 3.2.5 on 2021-12-28 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licznik', '0007_auto_20211228_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kandydat',
            name='email_confirmed',
        ),
        migrations.RemoveField(
            model_name='kandydat',
            name='user',
        ),
    ]
