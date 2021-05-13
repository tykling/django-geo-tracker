from django.contrib.gis.db import models
from django.core.serializers.json import DjangoJSONEncoder
import uuid

class Location(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tracker = models.ForeignKey("tracker.Tracker", on_delete=models.PROTECT)
    metadata = models.JSONField(encoder=DjangoJSONEncoder, decoder=DjangoJSONEncoder)
    location = models.PointField(editable=True, srid=4326)
