# Generated by Django 5.1.7 on 2025-04-08 18:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muebles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propietario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='telefono',
        ),
        migrations.AddField(
            model_name='propietario',
            name='nombre_empresa',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='propietario',
            name='tipo',
            field=models.CharField(choices=[('individual', 'Individual'), ('empresa', 'Empresa')], default='individual', max_length=10),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
