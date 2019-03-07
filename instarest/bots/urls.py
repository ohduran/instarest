from rest_framework import routers

from .views import BotViewSet

router = routers.SimpleRouter()
router.register(r'', BotViewSet)

app_name = 'bots'
urlpatterns = router.urls
