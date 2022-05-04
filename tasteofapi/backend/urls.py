from django.urls import include, path

from rest_framework import routers

from .views import MainScoreView, InstrumentView, ActorView

router = routers.DefaultRouter()
router.register(r'', MainScoreView)
router.register(r'instrument', InstrumentView, basename='instrument/')
router.register(r'actor', ActorView, basename='actor/')

urlpatterns = [
   path('', MainScoreView.as_view()),
   path('instrument', InstrumentView.as_view()),
   path('actor', ActorView.as_view())
]
