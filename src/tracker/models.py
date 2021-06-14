from django.db import models
import uuid
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse
from django.conf import settings
from binascii import unhexlify


class Tracker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(help_text="Human readable name for this tracker")
    description = models.TextField(help_text="Description of this tracker")
    metadata = models.JSONField(encoder=DjangoJSONEncoder, default=dict, help_text="Extra metadata about the tracker.")
    lora_device_eui = models.CharField(max_length=16, help_text="LoRa device EUI for the tracker.")
    lora_device_addr = models.CharField(max_length=8, help_text="LoRa device address (8 bytes).")
    lora_app_session_key = models.UUIDField(default=uuid.uuid4, help_text="LoRa ABP application session key (32 bytes).")
    lora_network_session_key = models.UUIDField(default=uuid.uuid4, help_text="LoRa ABP network session key (32 bytes).")

    def save(self):
        if not self.lora_device_eui:
            # derive DevEUI from Tracker UUID
            self.lora_device_eui = self.id.hex[0:16]

        if not self.lora_device_addr:
            # derive DevAddr from Tracker UUID
            self.lora_device_addr = self.id.hex[0:8]

        return super().save()

    def get_absolute_url(self):
        return reverse('tracker_detail', kwargs={'tracker_uuid' : self.pk})

    def lora_device_addr_bytearray(self):
        return [f"0x{x:02x}" for x in unhexlify(self.lora_device_addr)]

    def lora_network_session_key_bytearray(self):
        return [f"0x{x:02x}" for x in unhexlify(self.lora_network_session_key.hex)]

    def lora_app_session_key_bytearray(self):
        return [f"0x{x:02x}" for x in unhexlify(self.lora_app_session_key.hex)]
