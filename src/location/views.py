from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Location
from tracker.models import Tracker
from django.contrib.gis.geos import Point
from django.http import HttpResponse, HttpResponseBadRequest

class LocationPostView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, **kwargs):
        try:
            data = json.loads(request.POST["geojson"])
            loc = Location.objects.create(
                tracker=Tracker.objects.get(id=kwargs["tracker_uuid"]),
                metadata=data["properties"],
                location=Point(data["geometry"]["coordinates"]),
                timestamp=data["properties"]["payload"]["rxInfo"][0]["time"],
            )
        except:
            # probably bad/no location / no fix
            return HttpResponseBadRequest("Something is fucky")

        return HttpResponse("OK")
