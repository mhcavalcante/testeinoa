from django.contrib import admin

from testeinoa.models import Asset, PriceHistory

class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_code', 'tunel_max','tunel_min','update_frequency', 'email')

class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('asset_code', 'price', 'update_time', 'asset')

admin.site.register(Asset, AssetAdmin)
admin.site.register(PriceHistory, PriceHistoryAdmin)