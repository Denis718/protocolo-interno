# Generated by Django 3.2.16 on 2023-07-06 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinculo', '0002_alter_vinculo_data_fim'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinculo',
            name='matricula',
            field=models.IntegerField(null=True),
        ),
    ]