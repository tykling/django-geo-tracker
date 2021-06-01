from django.contrib import admin
from django.urls import path
from tracker.views import TrackerDetailView, TrackerListView
from location.views import LocationPostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tracker/', TrackerListView.as_view(), name="tracker_list"),
    path('tracker/<uuid:tracker_uuid>/', TrackerDetailView.as_view(), name="tracker_detail"),
    path('tracker/<uuid:tracker_uuid>/post_location/', LocationPostView.as_view(), name="post_location"),
]
