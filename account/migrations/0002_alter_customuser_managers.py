# Generated by Django 3.2.16 on 2023-06-15 13:37

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', account.models.CustomUserManager()),
            ],
        ),
    ]