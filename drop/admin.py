from django.contrib import admin

from .models import Drop


class DropModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "pub_date"]
    list_display_links = ["__str__", "pub_date"]
    list_filter = ["pub_date"]
    search_fields = ["name", "drop_description"]

    class Meta:
        model = Drop


admin.site.register(Drop, DropModelAdmin)
