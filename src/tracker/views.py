from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Tracker
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import redirect
from datetime import timedelta
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse


class TrackerListView(ListView):
    model = Tracker
    paginate_by = 100
    template_name = "tracker_list.html"


class TrackerDetailView(DetailView):
    model = Tracker
    template_name = "tracker_detail.html"
    pk_url_kwarg = "tracker_uuid"

    def get(self, request, *args, **kwargs):
        if not self.request.GET.get('not_before') and not self.request.GET.get('not_after'):
            not_before = (timezone.localtime(timezone.now()) - timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M")
            not_after = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M")
            return(redirect(reverse("tracker_detail", kwargs={"tracker_uuid": self.get_object().id}) + f"?not_before={not_before}&not_after={not_after}"))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locations = self.get_object().location_set.all()
        if self.request.GET.get('not_before'):
            locations = locations.filter(timestamp__gt=self.request.GET.get('not_before'))
            context["not_before"] = self.request.GET.get("not_before")
        if self.request.GET.get('not_after'):
            locations = locations.filter(timestamp__lt=self.request.GET.get('not_after'))
            context["not_after"] = self.request.GET.get("not_after")
        context["now"] = timezone.now()
        context["locations"] = locations
        context["total_locations"] = locations.count()
        context["geojson"] = GeoJSONSerializer().serialize(locations, use_natural_keys=True, with_modelname=False, geometry_field="location", precision=10)
        context["kftoken"] = settings.KORTFORSYNINGEN_TOKEN
        return context


class TrackerCreateView(CreateView):
    model = Tracker
    template_name = "tracker_create.html"
    fields = ["name", "description"]


class TrackerConfigView(DetailView):
    model = Tracker
    pk_url_kwarg = "tracker_uuid"

    def get(self, request, *args, **kwargs):
        context = {
            "name": self.get_object().name,
            "description": self.get_object().description,
            "lora_device_address": self.get_object().lora_device_addr_bytearray(),
            "lora_network_session_key": self.get_object().lora_network_session_key_bytearray(),
            "lora_app_session_key": self.get_object().lora_app_session_key_bytearray(),
            "sleep_seconds": settings.TRACKER_SLEEP_SECONDS,
        }
        rendered = render_to_string('tracker_config.py', context)
        response = HttpResponse(rendered, content_type="text/x-python")
        response['Content-Disposition'] = "attachment; filename=config.py"
        return response
