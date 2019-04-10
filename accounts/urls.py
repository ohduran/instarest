from rest_framework import routers

from .views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'', AccountViewSet)

app_name = 'accounts'
urlpatterns = router.urls
