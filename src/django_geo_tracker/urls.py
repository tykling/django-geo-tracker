from django.contrib import admin
from django.urls import path
from tracker.views import TrackerDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tracker/<uuid:tracker_uuid>/', TrackerDetailView.as_view(), name="tracker_detail"),
]
