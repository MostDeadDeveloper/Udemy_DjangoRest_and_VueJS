from django.urls import include, path
from rest_framework.routers import DefaultRouter
from profiles.api.views import (AvatarUpdateView, ProfileViewSet,
                                ProfileStatusViewSet)

router = DefaultRouter()
router.register("profiles", ProfileViewSet)
router.register("status", ProfileStatusViewSet, basename="status")

urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update")
]
