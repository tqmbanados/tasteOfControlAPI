from django.urls import include, path

from rest_framework import routers

from .views import MainScoreView, InstrumentView

router = routers.DefaultRouter()
router.register(r'', MainScoreView)
router.register(r'instrument', InstrumentView)

urlpatterns = [
   path('', include(router.urls)),
]