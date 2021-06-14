from django.contrib import admin
from django.urls import path
from tracker.views import TrackerDetailView, TrackerListView, TrackerCreateView, TrackerConfigView
from location.views import LocationPostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tracker/', TrackerListView.as_view(), name="tracker_list"),
    path('tracker/create/', TrackerCreateView.as_view(), name="tracker_create"),
    path('tracker/<uuid:tracker_uuid>/', TrackerDetailView.as_view(), name="tracker_detail"),
    path('tracker/<uuid:tracker_uuid>/post_location/', LocationPostView.as_view(), name="post_location"),
    path('tracker/<uuid:tracker_uuid>/download_config/', TrackerConfigView.as_view(), name="tracker_config"),
]
