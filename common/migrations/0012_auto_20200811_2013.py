# Generated by Django 3.0.8 on 2020-08-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_config'),
    ]

    operations = [
        migrations.CreateModel(
            name='homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='config',
        ),
    ]
