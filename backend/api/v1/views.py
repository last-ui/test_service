from api.v1.mixins import BaseListCreateDeleteViewSet
from picture.models import Picture


class PictureViewSet(BaseListCreateDeleteViewSet):
    """Представление модели Picture."""

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
