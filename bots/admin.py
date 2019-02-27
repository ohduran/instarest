from django.contrib import admin

from .models import Bot


@admin.register(Bot)
class BotModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'is_verified')
