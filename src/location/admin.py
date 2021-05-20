from django.contrib import admin
from .models import Location
from leaflet.admin import LeafletGeoAdmin

class LocationAdmin(LeafletGeoAdmin):
    list_display = ["uuid", "timestamp", "metadata"]
    list_filter = ["tracker__name"]

admin.site.register(Location, LocationAdmin)

