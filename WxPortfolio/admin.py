from django.contrib import admin
from .models import TransactionCurrency , Coins


class CoinsAdmin(admin.ModelAdmin):
    list_display = ['basename','fullname','code','tc']
    search_fields = ("basename",)
    ordering = 'basename',

class TcAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Coins, CoinsAdmin)
admin.site.register(TransactionCurrency,TcAdmin)