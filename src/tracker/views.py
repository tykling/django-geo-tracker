from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tracker
from djgeojson.serializers import Serializer as GeoJSONSerializer

class TrackerListView(ListView):
    model = Tracker
    paginate_by = 100
    template_name = "tracker_list.html"


class TrackerDetailView(DetailView):
    model = Tracker
    template_name = "tracker_detail.html"
    pk_url_kwarg = "tracker_uuid"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locations = self.get_object().location_set.all()
        if self.request.GET.get('not_before'):
            locations = locations.filter(timestamp__gt=self.request.GET.get('not_before'))
        if self.request.GET.get('not_after'):
            locations = locations.filter(timestamp__lt=self.request.GET.get('not_after'))
        context["locations"] = locations
        context["total_locations"] = locations.count()
        context["geojson"] = GeoJSONSerializer().serialize(locations, use_natural_keys=True, with_modelname=False, geometry_field="location")
        return context
