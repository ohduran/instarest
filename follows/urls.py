from rest_framework import routers

from .views import FollowViewSet

router = routers.SimpleRouter()
router.register(r'', FollowViewSet)
urlpatterns = router.urls
