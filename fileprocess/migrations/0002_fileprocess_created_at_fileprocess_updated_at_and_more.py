# Generated by Django 5.1 on 2024-08-27 13:44

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileprocess', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='fileprocess',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 27, 13, 44, 56, 945880)),
        ),
        migrations.AddField(
            model_name='fileprocess',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 27, 13, 44, 56, 945891)),
        ),
        migrations.AlterField(
            model_name='fileprocess',
            name='file_created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filesm', to=settings.AUTH_USER_MODEL),
        ),
    ]
