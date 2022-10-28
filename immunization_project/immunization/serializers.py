from rest_framework import serializers
from .models import Immunizations

class ImmunizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Immunizations
        fields = '__all__'