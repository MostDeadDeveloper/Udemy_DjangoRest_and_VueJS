from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from job_board.models import JobOffer
from .serializers import JobOfferSerializer


class JobOfferCreateAPIView(APIView):

    def get(self, request):
        joboffers = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(joboffers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobOfferDetailAPIView(APIView):

    def get_object(self, pk):
        joboffer = get_object_or_404(JobOffer, pk=pk)
        return joboffer

    def get(self, request, pk):
        joboffer = self.get_object(pk)
        serializer = JobOfferSerializer(joboffer)
        return Response(serializer.data)

    def put(self, request, pk):
        joboffer = self.get_object(pk)
        serializer = JobOfferSerializer(joboffer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        joboffer = self.get_object(pk)
        joboffer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
