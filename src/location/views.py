from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Location
from tracker.models import Tracker
from django.contrib.gis.geos import Point
from django.http import HttpResponse

class LocationPostView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, **kwargs):
        print(request.POST)
        data = json.loads(request.POST["geojson"])
        try:
            loc = Location.objects.create(
                tracker=Tracker.objects.get(uuid=kwargs["tracker_uuid"]),
                metadata=data["properties"],
                location=Point(data["geometry"]["coordinates"]),
                timestamp=data["properties"]["payload"]["rxInfo"][0]["time"],
            )
        except:
            # probably bad/no location / no fix
            return HttpResponseBadRequest("Something is fucky")

        return HttpResponse("OK")
