# Generated by Django 5.1 on 2024-08-27 11:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FileProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_serial_number', models.CharField(max_length=255, unique=True)),
                ('file_name', models.CharField(max_length=255)),
                ('file_content', models.TextField()),
                ('file_status', models.CharField(choices=[('start', 'Start'), ('checked', 'Checked'), ('scanned', 'Scanned'), ('recorded', 'Recorded')], default='start', max_length=10)),
                ('file_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
