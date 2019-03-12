from rest_framework import routers

from .views import FollowedViewSet

router = routers.SimpleRouter()
router.register(r'', FollowedViewSet)

app_name = 'follows'
urlpatterns = router.urls
