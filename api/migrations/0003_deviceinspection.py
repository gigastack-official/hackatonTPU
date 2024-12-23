# Generated by Django 4.2.16 on 2024-12-06 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_device_lightingmode_measurement_sensor_delete_post_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceInspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked', models.BooleanField(default=False)),
                ('last_checked_at', models.DateTimeField(blank=True, null=True)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inspection', to='api.device')),
            ],
        ),
    ]
