from django.contrib import admin
from gift_registry.models import Gift, Giver

class GiftAdmin(admin.ModelAdmin):
    list_display = ('title', 'one_only', 'live')
    list_filter = ('live',)


class GiverAdmin(admin.ModelAdmin):
    list_display = ('email', 'gift')


admin.site.register(Gift, GiftAdmin)
admin.site.register(Giver, GiverAdmin)
