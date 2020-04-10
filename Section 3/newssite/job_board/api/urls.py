from django.urls import path
from job_board.api.views import (JobOfferCreateAPIView, JobOfferDetailAPIView)


urlpatterns = [
    path("jobs/",
         JobOfferCreateAPIView.as_view(),
         name="job-list"),

    path("jobs/<int:pk>/",
         JobOfferDetailAPIView.as_view(),
         name="job-detail"),

]
