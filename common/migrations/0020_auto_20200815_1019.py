# Generated by Django 3.0.8 on 2020-08-15 02:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0019_steps_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workf',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work', to=settings.AUTH_USER_MODEL),
        ),
    ]