from django.db import models
import uuid
from django.core.serializers.json import DjangoJSONEncoder

class Tracker(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(help_text="Human readable name for this tracker")
    description = models.TextField(help_text="Description of this tracker")
    metadata = models.JSONField(encoder=DjangoJSONEncoder, help_text="Extra metadata about the tracker.")
