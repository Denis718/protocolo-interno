# Generated by Django 3.2.16 on 2023-05-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('classe', models.CharField(max_length=60)),
                ('jornada', models.IntegerField()),
            ],
        ),
    ]