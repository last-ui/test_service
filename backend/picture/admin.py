from django.contrib import admin

from picture.models import Picture


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    """Управление картинками."""

    list_display = ("description",)
    search_fields = ("description",)
