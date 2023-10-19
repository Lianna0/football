from django.contrib import admin

# Register your models here.

from .models import Player, Club


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','country','age','position','club', 'foot')
    list_display_links = ('name',)
    search_fields = ('country', 'club',)
    list_filter = ('position',)

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'league', 'stadium')
    list_display_links = ('name',)