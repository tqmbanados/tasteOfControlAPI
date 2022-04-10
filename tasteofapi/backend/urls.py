from django.urls import include, path

from rest_framework import routers

from .views import MainScoreView, InstrumentView, ActorView

router = routers.DefaultRouter()
router.register(r'', MainScoreView)
router.register(r'instrument', InstrumentView)
router.register(r'actor', ActorView)

urlpatterns = [
   path('', include(router.urls)),
]