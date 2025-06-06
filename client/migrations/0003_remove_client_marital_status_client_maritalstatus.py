# Generated by Django 5.2 on 2025-04-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_marital_status_alter_client_createdat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='marital_status',
        ),
        migrations.AddField(
            model_name='client',
            name='maritalStatus',
            field=models.CharField(choices=[('single', 'Solteiro(a)'), ('married', 'Casado(a)'), ('divorced', 'Divorciado(a)'), ('widowed', 'Viúvo(a)'), ('separated', 'Separado(a)')], default='single', max_length=20, verbose_name='Estado civil'),
        ),
    ]
