from rest_framework import serializers
from job_board.models import JobOffer


class JobOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobOffer
        fields = "__all__"
