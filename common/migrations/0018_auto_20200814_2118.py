# Generated by Django 3.0.8 on 2020-08-14 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0017_auto_20200814_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='steps',
            old_name='state',
            new_name='nextstate',
        ),
    ]
