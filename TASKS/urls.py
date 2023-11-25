from rest_framework import routers
# Create your views here.
from .views import CarListAPIview

router = routers.DefaultRouter()
router.register("list",CarListAPIview,basename='man')
urlpatterns = router.urls