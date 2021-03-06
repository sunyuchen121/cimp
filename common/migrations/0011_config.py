# Generated by Django 3.0.8 on 2020-08-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_paper'),
    ]

    operations = [
        migrations.CreateModel(
            name='config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='homepage', max_length=10)),
                ('news', models.ManyToManyField(to='common.news')),
                ('notice', models.ManyToManyField(to='common.notice')),
                ('paper', models.ManyToManyField(to='common.paper')),
            ],
        ),
    ]
