from rest_framework import generics
from quotes.models import Quote
from quotes.api.permissions import IsAdminUserOrReadOnly
from quotes.api.serializers import Quoteserializer
from .pagination import QuotePagination


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("id")
    serializer_class = Quoteserializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = QuotePagination


class QuoteDetailAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = Quoteserializer
    pagination_class = QuotePagination
    permission_classes = [IsAdminUserOrReadOnly]
