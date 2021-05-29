from django.db import models
import uuid
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse


class Tracker(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(help_text="Human readable name for this tracker")
    description = models.TextField(help_text="Description of this tracker")
    metadata = models.JSONField(encoder=DjangoJSONEncoder, help_text="Extra metadata about the tracker.")


    def get_absolute_url(self):
        return reverse('tracker_detail', kwargs={'tracker_uuid' : self.pk})
