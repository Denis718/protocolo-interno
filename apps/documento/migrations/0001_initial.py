# Generated by Django 3.2.16 on 2023-04-28 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id_documento', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('descricao', models.CharField(max_length=60)),
                ('utiliza_num_ano', models.BooleanField()),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('modifyAt', models.DateTimeField(blank=True, null=True)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentos_criados', to=settings.AUTH_USER_MODEL)),
                ('modifyBy', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documentos_modificados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
