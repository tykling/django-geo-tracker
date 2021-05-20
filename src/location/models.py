from django.contrib.gis.db import models
from django.core.serializers.json import DjangoJSONEncoder
import uuid
from django.utils import timezone


class Location(models.Model):
    class Meta:
        ordering = ["timestamp"]

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tracker = models.ForeignKey("tracker.Tracker", on_delete=models.PROTECT)
    metadata = models.JSONField(encoder=DjangoJSONEncoder)
    location = models.PointField(editable=True, srid=4326)
    timestamp = models.DateTimeField(
        default=timezone.now,
        help_text="The timestamp of this location",
    )
