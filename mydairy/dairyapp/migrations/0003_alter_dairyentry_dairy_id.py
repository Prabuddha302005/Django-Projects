# Generated by Django 5.0.1 on 2024-07-13 15:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0002_dairyentry_dairy_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='dairyentry',
            name='dairy_id',
            field=models.ForeignKey(db_column='dairy_id', default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
