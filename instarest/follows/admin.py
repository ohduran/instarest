from django.contrib import admin

from .models import Followed


@admin.register(Followed)
class FollowedModelAdmin(admin.ModelAdmin):
    list_display = ('username',)
