# Generated by Django 4.2.16 on 2024-12-06 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('device_type', models.CharField(choices=[('pump', 'Pump'), ('fan', 'Fan'), ('servo', 'Servo (door/window)'), ('led', 'LED Strip')], max_length=20)),
                ('is_active', models.BooleanField(default=False)),
                ('brightness', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LightingMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('fluid_level', models.FloatField(blank=True, null=True)),
                ('co2', models.FloatField(blank=True, null=True)),
                ('humidity', models.FloatField(blank=True, null=True)),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('illumination', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('volume', models.FloatField(blank=True, null=True)),
                ('fluid_level', models.FloatField(blank=True, null=True)),
                ('leakage', models.BooleanField(default=False)),
                ('fill_level', models.FloatField(blank=True, null=True)),
                ('illumination', models.FloatField(blank=True, null=True)),
                ('voc', models.FloatField(blank=True, null=True)),
                ('co2', models.FloatField(blank=True, null=True)),
                ('humidity', models.FloatField(blank=True, null=True)),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('energy_consumption', models.FloatField(blank=True, null=True)),
                ('gyro_data', models.CharField(blank=True, max_length=100, null=True)),
                ('accelerometer_data', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='api.sensor'),
        ),
    ]