# Generated by Django 4.2.16 on 2024-12-06 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_command'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='user_name',
        ),
        migrations.AddField(
            model_name='command',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='commands', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='command',
            name='command_type',
            field=models.CharField(choices=[('pump', 'Помпа'), ('led', 'Лента'), ('servo1', 'Серво №1'), ('servo2', 'Серво №2'), ('auto_light', 'Авто-свет'), ('brightness', 'Яркость'), ('fan', 'Вентилятор'), ('ventilation', 'Проветривание')], max_length=20),
        ),
    ]
