from rest_framework.routers import DefaultRouter

from api.v1.views import PictureViewSet

app_name = "v1"

router_v1 = DefaultRouter()

router_v1.register("employment", PictureViewSet, basename="employment")
