# Generated by Django 5.1.7 on 2025-04-09 15:22

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muebles', '0002_remove_propietario_email_remove_propietario_nombre_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propietario',
            options={'ordering': ['-fecha_registro'], 'verbose_name': 'Propietario', 'verbose_name_plural': 'Propietarios'},
        ),
        migrations.AddField(
            model_name='propietario',
            name='fecha_registro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='propietario',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='tipo',
            field=models.CharField(choices=[('individual', 'Propietario Individual'), ('empresa', 'Empresa')], max_length=10),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propietario', to=settings.AUTH_USER_MODEL),
        ),
    ]
