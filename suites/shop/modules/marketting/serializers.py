from rest_framework import serializers

from .models import Campaign, CampaignCodeConfig


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'

class CampaignCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignCodeConfig
        fields = '__all__'