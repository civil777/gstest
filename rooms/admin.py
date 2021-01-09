from django.contrib import admin
from . import models
from django.utils.html import mark_safe

@admin.register(models.RoomType)
class ItemAdmin(admin.ModelAdmin):
    pass

class PhotoInline(admin.TabularInline):

    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    list_display = (
        "name", "price", "item_type", "special_item", "total_rating",
    )
    list_filter = ("item_type", "special_item",)

    seaerch_fields = ("name", "^host__username",)

    ordering = ("name", "price", )

    raw_id_fields = ("host",)

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="70px" src="{obj.file.url}" />')
