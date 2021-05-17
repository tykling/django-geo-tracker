from django.contrib import admin
from .models import Location
from leaflet.admin import LeafletGeoAdmin

class LocationAdmin(LeafletGeoAdmin):
    list_display = ["tracker_id", "timestamp", "metadata"]
    list_filter = ["tracker__name"]

admin.site.register(Location, LocationAdmin)

