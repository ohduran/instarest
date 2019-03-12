from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('docs/', include_docs_urls(title='InstaREST')),
    path(
        "users/",
        include("users.urls", namespace="users"),
    ),
    path(
        'auth/',
        include('djoser.urls')),
    path('follows/', include('follows.urls', namespace='follows')),
    path('auth/', include('djoser.urls.authtoken')),
    path('bots/', include('bots.urls', namespace='bots')),

]
