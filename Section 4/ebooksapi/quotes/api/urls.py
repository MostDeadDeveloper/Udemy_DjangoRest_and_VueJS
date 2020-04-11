from django.urls import path
from quotes.api.views import (QuoteListCreateAPIView, QuoteDetailAPIview)


urlpatterns = [
    path("quotes/",
         QuoteListCreateAPIView.as_view(),
         name="quotes-list"),

    path("quotes/<int:pk>/",
         QuoteDetailAPIview.as_view(),
         name="quotes-detail"),


]
