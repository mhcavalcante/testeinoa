from django.contrib import admin

from testeinoa.models import Stock, PriceHistory

class StockAdmin(admin.ModelAdmin):
    list_display = ('stock_code', 'tunel_max','tunel_min','update_frequency', 'email')

class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('stock_code', 'price', 'update_time', 'stock')

admin.site.register(Stock, StockAdmin)
admin.site.register(PriceHistory, PriceHistoryAdmin)