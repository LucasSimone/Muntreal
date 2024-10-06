# Generated by Django 4.2.9 on 2024-02-01 02:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_rename_deploymenttemplate_deployment'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='deployment_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deployment',
            name='deployment_date',
            field=models.DateField(),
        ),
    ]
