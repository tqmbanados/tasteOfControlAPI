from django.urls import include, path

from rest_framework import routers

from .views import MainScoreView

router = routers.DefaultRouter()
router.register(r'', MainScoreView)

urlpatterns = [
   path('', include(router.urls)),
]