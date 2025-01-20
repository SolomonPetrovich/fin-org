from rest_framework import serializers

from .models import FinancialOrganization, FinancialOrganizationNews


class FinancialOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialOrganization
        fields = '__all__'
        
        
class FinancialOrganizationNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialOrganizationNews
        fields = '__all__'