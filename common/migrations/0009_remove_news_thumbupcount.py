# Generated by Django 3.0.8 on 2020-08-10 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_news_thumbupcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='thumbupcount',
        ),
    ]
