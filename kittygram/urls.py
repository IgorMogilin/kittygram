from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cats.views import CatViewset, OwnerViewset

router = DefaultRouter()
router.register('cats', CatViewset)
router.register('owners', OwnerViewset)

urlpatterns = [
    path('', include(router.urls))
]
