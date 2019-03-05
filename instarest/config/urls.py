from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        "users/",
        include("users.urls", namespace="users"),
    ),
    path(
        'auth/',
        include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
