from django.contrib import admin

from .models import Account


@admin.register(Account)
class BotModelAdmin(admin.ModelAdmin):
    list_display = ('username',)
