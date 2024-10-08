# Generated by Django 5.1 on 2024-08-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('staff', 'Staff'), ('user', 'User')], default='staff', max_length=20, verbose_name='Role'),
        ),
    ]
