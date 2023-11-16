from api.v1.mixins import BaseListCreateDeleteViewSet
from api.v1.serializers import PictureSerializer
from picture.models import Picture


class PictureViewSet(BaseListCreateDeleteViewSet):
    """Представление модели Picture."""

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
