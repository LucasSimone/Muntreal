# Generated by Django 4.2.16 on 2024-10-08 23:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('date_recieved', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('content', models.TextField()),
                ('priority', models.IntegerField(choices=[(0, 'New'), (1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'None')], default=0)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('content', models.TextField()),
                ('date_recieved', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('camera', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('people', models.ManyToManyField(related_name='model', to='main_site.person')),
                ('photographer', models.ManyToManyField(related_name='photographer', to='main_site.person')),
            ],
            options={
                'verbose_name_plural': 'Images',
            },
        ),
    ]
