# Generated by Django 3.2.2 on 2021-06-14 16:06

import django.core.serializers.json
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_tracker_metadata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='uuid',
            new_name='id',
        ),
        migrations.AddField(
            model_name='tracker',
            name='lora_app_session_key',
            field=models.UUIDField(default=uuid.uuid4, help_text='LoRa ABP application session key (32 bytes).'),
        ),
        migrations.AddField(
            model_name='tracker',
            name='lora_device_addr',
            field=models.CharField(default=123, help_text='LoRa device address (8 bytes).', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tracker',
            name='lora_device_eui',
            field=models.CharField(default=123, help_text='LoRa device EUI for the tracker.', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tracker',
            name='lora_network_session_key',
            field=models.UUIDField(default=uuid.uuid4, help_text='LoRa ABP network session key (32 bytes).'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='metadata',
            field=models.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, help_text='Extra metadata about the tracker.'),
        ),
    ]