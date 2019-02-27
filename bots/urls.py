from rest_framework import routers

from .views import BotViewSet

router = routers.SimpleRouter()
router.register(r'', BotViewSet)
urlpatterns = router.urls
