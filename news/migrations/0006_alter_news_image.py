# Generated by Django 5.1 on 2024-09-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_ticketannouncement_last_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.JSONField(default=list),
        ),
    ]
